"""Generate deterministic browser data for the GPry and SIGWAY explainers."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "src" / "data"
DATA.mkdir(parents=True, exist_ok=True)


def target(x: np.ndarray) -> np.ndarray:
    """A smooth, asymmetric two-feature log posterior."""
    left = -0.5 * ((x + 1.45) / 0.58) ** 2
    right = -0.5 * ((x - 1.2) / 0.36) ** 2 - 0.52
    return np.logaddexp(left, right) - 0.12 * np.sin(1.7 * x)


def gp_predict(x_train: np.ndarray, y_train: np.ndarray, x: np.ndarray):
    ell, noise = 0.72, 2e-5
    kernel = lambda a, b: np.exp(-0.5 * ((a[:, None] - b[None, :]) / ell) ** 2)
    kxx = kernel(x_train, x_train) + noise * np.eye(len(x_train))
    alpha = np.linalg.solve(kxx, y_train)
    cross = kernel(x_train, x)
    mean = cross.T @ alpha
    variance = np.maximum(1 - np.sum(cross * np.linalg.solve(kxx, cross), axis=0), 1e-8)
    return mean, np.sqrt(variance)


def generate_gpry():
    x = np.linspace(-4.0, 4.0, 181)
    truth = target(x)
    selected = [12, 168, 90]
    states = []
    for iteration in range(16):
        xt = x[selected]
        yt = truth[selected]
        mean, std = gp_predict(xt, yt, x)
        density = np.exp(mean - np.max(mean))
        acquisition = std * (0.18 + density)
        acquisition[np.array(selected)] = -1
        next_index = int(np.argmax(acquisition))
        states.append({
            "iteration": iteration,
            "selected": selected.copy(),
            "mean": np.round(mean, 5).tolist(),
            "std": np.round(std, 5).tolist(),
            "acquisition": np.round(np.maximum(acquisition, 0), 5).tolist(),
            "next": next_index,
        })
        selected.append(next_index)
    payload = {
        "convention": "Illustrative deterministic RBF-GP active-learning sequence; fixed seed-free grid.",
        "x": np.round(x, 5).tolist(),
        "truth": np.round(truth, 5).tolist(),
        "states": states,
    }
    (DATA / "gpry-toy.json").write_text(json.dumps(payload, separators=(",", ":")))


def target_2d(points: np.ndarray) -> np.ndarray:
    """Curved primary mode plus a smaller separated feature."""
    x, y = points[:, 0], points[:, 1]
    main = -0.5 * ((x / 1.28) ** 2 + ((y - 0.34 * x**2 + 0.58) / 0.56) ** 2)
    satellite = -0.5 * (((x - 1.72) / 0.48) ** 2 + ((y - 1.32) / 0.42) ** 2) - 1.45
    return np.logaddexp(main, satellite)


def gp_predict_2d(x_train: np.ndarray, y_train: np.ndarray, points: np.ndarray):
    """Fixed anisotropic RBF GP with a conservative off-data prior mean."""
    ell = np.array([0.82, 0.72])
    noise, prior_mean = 2e-3, -13.0

    def kernel(a, b):
        delta = (a[:, None, :] - b[None, :, :]) / ell
        squared_distance = np.minimum(np.sum(delta**2, axis=2), 60.0)
        return np.exp(-0.5 * squared_distance)

    kxx = kernel(x_train, x_train) + noise * np.eye(len(x_train))
    cross = kernel(x_train, points)
    solve = np.linalg.solve(kxx, cross)
    alpha = np.linalg.solve(kxx, y_train - prior_mean)
    mean = prior_mean + np.sum(cross * alpha[:, None], axis=0)
    variance = np.maximum(1.0 - np.sum(cross * solve, axis=0), 1e-8)
    return mean, np.sqrt(variance)


def generate_gpry_2d():
    """Precompute a deterministic NORA-style batch-acquisition sequence.

    NORA explores samples distributed as the GP-mean posterior, evaluates the
    GPry LogExp acquisition on that pool, and uses sequential conditioning for
    a parallel batch. Here the mean-posterior sample is drawn deterministically
    from a dense grid; the browser performs no fitting.
    """
    rng = np.random.default_rng(24052023)
    n_grid = 49
    axis = np.linspace(-3.2, 3.2, n_grid)
    xx, yy = np.meshgrid(axis, axis)
    grid = np.column_stack([xx.ravel(), yy.ravel()])
    truth = target_2d(grid)
    evaluated = np.array([
        [-2.75, -2.45], [2.70, -2.35], [-2.65, 2.50], [2.65, 2.55],
        [-0.75, -0.70], [0.65, 0.05], [1.85, 1.45], [0.05, 2.35],
    ])
    values = target_2d(evaluated)
    states = []
    zeta = 2 ** (-0.85)  # GPry LogExp automatic scaling in two dimensions.
    for iteration in range(8):
        mean, std = gp_predict_2d(evaluated, values, grid)
        with np.errstate(divide="ignore"):
            acquisition = 2 * zeta * (mean - np.max(values)) + np.log(np.maximum(std, 1e-8))

        # Deterministic approximation to NORA's mean-posterior nested-sampling cloud.
        weights = np.exp(np.clip(mean - np.max(mean), -40, 0))
        weights /= weights.sum()
        density_idx = rng.choice(len(grid), size=260, replace=True, p=weights)
        uniform_idx = rng.choice(len(grid), size=70, replace=False)
        candidate_idx = np.concatenate([density_idx, uniform_idx])
        candidates = grid[candidate_idx] + rng.normal(0, 0.025, (len(candidate_idx), 2))
        candidates = np.clip(candidates, axis[0], axis[-1])

        # Kriging-believer conditioning: after each choice, refit with its GP mean.
        batch = []
        fantasy_x, fantasy_y = evaluated.copy(), values.copy()
        for _ in range(4):
            c_mean, c_std = gp_predict_2d(fantasy_x, fantasy_y, candidates)
            with np.errstate(divide="ignore"):
                c_acq = 2 * zeta * (c_mean - np.max(fantasy_y)) + np.log(np.maximum(c_std, 1e-8))
            near = np.min(np.sum((candidates[:, None, :] - fantasy_x[None, :, :]) ** 2, axis=2), axis=1)
            c_acq[near < 0.0025] = -np.inf
            pick = int(np.argmax(c_acq))
            point = candidates[pick]
            batch.append(point.tolist())
            fantasy_x = np.vstack([fantasy_x, point])
            fantasy_y = np.append(fantasy_y, c_mean[pick])

        states.append({
            "iteration": iteration,
            "evaluated": np.round(evaluated, 4).tolist(),
            "mean": np.round(mean.reshape(n_grid, n_grid), 4).tolist(),
            "std": np.round(std.reshape(n_grid, n_grid), 4).tolist(),
            "acquisition": np.round(acquisition.reshape(n_grid, n_grid), 4).tolist(),
            "candidates": np.round(candidates, 4).tolist(),
            "batch": np.round(batch, 4).tolist(),
        })
        new_points = np.asarray(batch)
        evaluated = np.vstack([evaluated, new_points])
        values = np.append(values, target_2d(new_points))

    payload = {
        "convention": "Deterministic NORA-style replay: RBF GP, GPry LogExp acquisition, GP-mean posterior candidate sample, and sequential Kriging-believer batch ranking.",
        "bounds": [float(axis[0]), float(axis[-1])],
        "axis": np.round(axis, 4).tolist(),
        "truth": np.round(truth.reshape(n_grid, n_grid), 4).tolist(),
        "batchSize": 4,
        "states": states,
    }
    (DATA / "gpry-toy-2d.json").write_text(json.dumps(payload, separators=(",", ":")))


def generate_sigway():
    public = ROOT / "public" / "data"
    public.mkdir(parents=True, exist_ok=True)
    for nbins in (10, 50, 100):
        source = Path(
            f"/tmp/sigway-source/sigway/binning_coefficients/tabkpp{nbins}.txt"
        )
        data = np.loadtxt(source)
        knum, pnum = int(data[0]), int(data[1])
        fk = data[2 : 2 + knum]
        fp = data[2 + knum : 2 + knum + pnum]
        coeff = data[2 + knum + pnum :].reshape(knum, pnum, pnum)
        payload = {
            "source": f"SIGWAY main: sigway/binning_coefficients/tabkpp{nbins}.txt",
            "formula": "Omega[m] = 0.39 * 4.2e-5 * sum_ij C[m,i,j] A[i] A[j]",
            "normalization": 0.39 * 4.2e-5,
            "fk": fk.tolist(),
            "fp": fp.tolist(),
            "coeff": coeff.tolist(),
        }
        destination = public / f"sigway-kernel-{nbins}.json"
        destination.write_text(json.dumps(payload, separators=(",", ":")))
        if nbins == 10:
            (DATA / "sigway-kernel-10.json").write_text(
                json.dumps(payload, separators=(",", ":"))
            )


if __name__ == "__main__":
    generate_gpry()
    generate_gpry_2d()
    generate_sigway()
