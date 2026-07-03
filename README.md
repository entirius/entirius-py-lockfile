# lockfile

File-based lock (via `fcntl.flock`) preventing concurrent runs of the same process —
atomic across forked processes, unlike thread-level locks and semaphores.

## Installation

```shell
pip install entirius-py-lockfile
```

## Usage

```python
from lockfile import LockFile

lock = LockFile("/var/run/my-job.lock")
lock.acquire()          # raises if already held (non-blocking by default)
try:
    ...                 # critical section
finally:
    lock.release()
```

Pass `wait_for_acquire=True` to block until the lock is available instead of raising.

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest)
```

Development and agent instructions: [AGENTS.md](AGENTS.md).

## License

Mozilla Public License 2.0 — see [LICENSE](LICENSE).
