# entirius-py-lockfile

A file-based process lock built on `fcntl.flock`, part of Entirius, the open-source modular ecommerce platform. It
prevents concurrent runs of the same job and is atomic across forked processes, unlike thread-level locks and
semaphores.

[![PyPI](https://img.shields.io/pypi/v/entirius-py-lockfile.svg)](https://pypi.org/project/entirius-py-lockfile/)
[![Python](https://img.shields.io/pypi/pyversions/entirius-py-lockfile.svg)](https://pypi.org/project/entirius-py-lockfile/)
[![License: MPL-2.0](https://img.shields.io/badge/license-MPL--2.0-blue.svg)](https://github.com/entirius/entirius-py-lockfile/blob/develop/LICENSE)

## What it does

- Takes an exclusive lock on a lock file (`acquire()`); the file is created when it does not exist.
- Does not block by default: `acquire()` raises when the lock is already held.
- Waits for the lock instead of raising with `wait_for_acquire=True`.
- Releases the lock (`release()`).

## Installation

```shell
uv add entirius-py-lockfile
pip install entirius-py-lockfile
```

The import name is `lockfile`.

## Quick start

```python
from lockfile import LockFile

lock = LockFile("/var/run/my-job.lock")
lock.acquire()          # raises if already held (non-blocking by default)
try:
    ...                 # critical section
finally:
    lock.release()
```

## Requirements

- Python 3.11 or newer.
- A POSIX system: the lock uses the standard-library `fcntl` module.
- No runtime dependencies.

## Documentation

- Entirius documentation: https://docs.entirius.com/
- Changelog: https://github.com/entirius/entirius-py-lockfile/blob/develop/CHANGELOG.md

## Part of Entirius

This lock guards single-run jobs in the Entirius backend service (Volkanos) and its modules.

- Backend service: https://github.com/entirius/entirius-service-volkanos
- Docker harness: https://github.com/entirius/entirius-zeno
- Consumer modules: https://github.com/entirius/entirius-django-pim-csv, https://github.com/entirius/entirius-django-pricemanager

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest)
```

Development and agent instructions: https://github.com/entirius/entirius-py-lockfile/blob/develop/AGENTS.md

## License

Mozilla Public License 2.0 (MPL-2.0) — see https://github.com/entirius/entirius-py-lockfile/blob/develop/LICENSE.
