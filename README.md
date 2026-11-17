# CompressionTest

CompressionTest is a small Python utility for comparing four approximate reconstruction methods on a non-empty, two-dimensional numeric matrix. It reports relative Frobenius reconstruction error and a threshold-based pass flag; it does not measure compressed storage size.

The project is at an early utility/library stage (version 0.1.0 in `pyproject.toml`). Its tests cover basic behavior on synthetic smooth matrices and invalid inputs. It should not be treated as a general-purpose compression tool or a performance benchmark.

## Implemented methods

The `compressiontest` module provides:

- `svd_compress(matrix, rank=4)`: truncates a singular-value decomposition to the requested rank, capped at the available singular values.
- `quantize(matrix, bits=8)`: uniformly quantizes values over the input matrix's minimum-to-maximum range; supported bit settings are 1 through 16.
- `fourier_compress(matrix, num_coeffs=4)`: fits each row to a constant-plus-sine/cosine Fourier basis over the matrix's columns.
- `hybrid_compress(matrix, rank=4, bits=8)`: applies SVD truncation followed by quantization.
- `benchmark(matrix)`: runs SVD rank 4, 8-bit quantization, Fourier with 4 harmonics, and the rank-4/8-bit hybrid. It returns one dictionary per method with `method`, `relative_error`, and `passed`. The pass flag is `relative_error < 0.5`.

Inputs are converted to NumPy `float64`; compression and benchmark functions reject empty or non-2D matrices. `benchmark` defines the relative error as the Frobenius norm of the reconstruction difference divided by the input's Frobenius norm (and returns zero error for an all-zero input).

## Requirements and use

Python 3.9 or newer and NumPy 1.24 or newer are declared in `pyproject.toml`. From the repository root, install the listed dependencies:

```bash
python -m pip install -r requirements.txt
```

Import the module from the repository root and pass a matrix as a NumPy array:

```python
import numpy as np
from compressiontest import benchmark

matrix = np.array([[1.0, 2.0, 3.0], [2.0, 3.0, 4.0]])
for result in benchmark(matrix):
    print(result["method"], result["relative_error"], result["passed"])
```

There is no CLI, file input/output workflow, or command for compressing and saving data in the repository.

## Tests and CI

On commit `da4dab5572d504cb9436ae84b687c7051201559d` (the inspected `main` HEAD), `python3 -m pytest -q` completed successfully: **10 tests passed**. The GitHub Actions CI and CodeQL workflow runs associated with that same commit were also completed with a `success` conclusion when inspected. CI is configured for Python 3.10, 3.11, and 3.12; that matrix is narrower than the Python `>=3.9` declaration.

To run the test suite locally after installing dependencies:

```bash
python -m pytest -q
```

The tests exercise approximation behavior on generated smooth matrices, supported validation cases, and the shape of benchmark results. They do not establish broad accuracy across real datasets or demonstrate storage savings or runtime performance.

## Limitations

- The `passed` threshold of 0.5 is fixed in `benchmark` and is not configurable; it is not a use-case-specific quality target.
- Results report reconstruction error only. The code does not calculate encoded byte size, compression ratio, runtime comparisons, or downstream task accuracy.
- The tests use synthetic smooth matrices and do not provide a representative evaluation across data types or workloads.
- The Fourier approximation assumes a periodic basis along the column dimension; its suitability depends on the input.
- This repository does not provide a file format, serializer, command-line interface, or production compression/decompression pipeline.

## License

The repository includes an MIT License. See [LICENSE](LICENSE) for its terms and copyright notice.
