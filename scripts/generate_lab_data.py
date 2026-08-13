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
    generate_sigway()
