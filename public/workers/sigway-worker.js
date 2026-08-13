let kernel = null;

self.onmessage = async (event) => {
  if (event.data.type === 'load') {
    const response = await fetch(`/data/sigway-kernel-${event.data.nbins}.json`);
    kernel = await response.json();
    self.postMessage({ type: 'loaded', kernel: { fk: kernel.fk, fp: kernel.fp, normalization: kernel.normalization }, nbins: event.data.nbins });
    return;
  }
  if (event.data.type === 'calculate' && kernel) {
    const amplitudes = event.data.amplitudes;
    const omega = new Float64Array(kernel.fk.length);
    for (let m = 0; m < kernel.fk.length; m++) {
      const matrix = kernel.coeff[m];
      let sum = 0;
      for (let i = 0; i < amplitudes.length; i++) {
        const ai = amplitudes[i];
        for (let j = 0; j < amplitudes.length; j++) sum += matrix[i][j] * ai * amplitudes[j];
      }
      omega[m] = kernel.normalization * sum;
    }
    self.postMessage({ type: 'result', omega: Array.from(omega), token: event.data.token });
  }
};
