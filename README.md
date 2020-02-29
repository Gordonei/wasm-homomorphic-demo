# Web Assembly Homomorphic Encryption Demo

Fairly self-contained example of homomorphic encryption using Python (to encrypt) and WebAssembly (to do the operations).

The demo encrypts two values supplied by the user, generates Web Assembly code for doing the calculation (that has no knowledge of the true values), and validates the result.

## Setup
* [python-paillier library](https://github.com/n1analytics/python-paillier)
* [libpailier C library](https://github.com/mortendahl/libpaillier)
* [WebAssembly tool chain](https://webassembly.org/getting-started/developers-guide/)
* [GMPLib](https://gmplib.org/), compiled for WebAssembly. See [these instructions](https://stackoverflow.com/questions/41080815/compiling-gmp-mpfr-with-emscripten)

## Customisations
I had to alter `paillier.h` to include the GMP lib (i.e. `#include "<path to gmp.h>/gmp.h"`) upfront. This is probably me buggering up the `emcc` compile flags, though.

## Use
From the root of this repo, run `python3 bin/generate-encrypted-data.py <integer a, e.g. 1> <integer b, e.g. 2>`.
