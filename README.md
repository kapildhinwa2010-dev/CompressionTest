# CompressionTest

[![CI](https://github.com/kapildhinwa2010-dev/CompressionTest/actions/workflows/ci.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/CompressionTest/actions/workflows/ci.yml)
[![CI](https://github.com/kapildhinwa2010-dev/CompressionTest/actions/workflows/codeql.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/CompressionTest/actions/workflows/codeql.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Compression test harness: four strategies (SVD rank, quantization, Fourier basis, hybrid) with uniform error reporting.

**Part of the [Kapildhinwa2010-dev Toolkit](https://github.com/kapildhinwa2010-dev/Kapildhinwa2010-dev).**

## What it does

benchmark(matrix) runs all four strategies on one 2-D matrix and
returns per-method relative Frobenius error and a pass/fail flag at a
0.5 threshold. A test harness for the toolkit codecs, not a
production compressor.

## Install

    pip install -r requirements.txt

## Quick start

    from compressiontest import benchmark

    for result in benchmark(W):
        print(result["method"], result["relative_error"], result["passed"])

## API

- benchmark(matrix) - list of {method, relative_error, passed}

## Honest results and limitations

- The 0.5 "passed" threshold is arbitrary; real pipelines pick error
  budgets per use case.
- On random matrices every method has relative error near 1.0 - that
  is the expected honest outcome, not a bug.
- Storage size is NOT reported here (see Compression-Lib for byte
  estimates); error alone is not a compression metric.
- No task-accuracy evaluation: reconstruction error is the only
  quality measure.

## License

MIT - see [LICENSE](LICENSE).
