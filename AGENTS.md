# AGENTS.md

File-based process lock — distribution `entirius-py-lockfile`, import `lockfile`.

## Commands

| Command | Meaning |
|---|---|
| `make install` | sync dependencies (uv, incl. extras) |
| `make check` | lint + format-check (ruff) |
| `make fix` | auto-fix lint + format |
| `make test` | test suite (pytest) |

## Conventions

- English only: code, docs, commits, branches, PRs.
- MPL-2.0: every non-trivial source file carries the license header (pre-commit inserts it).
- Toolchain: uv + ruff + hatchling + pytest; all config in `pyproject.toml`; `uv.lock` committed.
- Git flow: `master` (production) + `develop` (integration); changes land via PR; semver tag on `master`.
- Never rename the import package `lockfile` — it is a public API contract.
- Default: do not commit — git is the user's call.

## Architecture

Single class `LockFile` in `lockfile/`: wraps `fcntl.flock` on an open file handle.
`acquire()` (non-blocking by default, or blocking with `wait_for_acquire=True`), `release()`.
No runtime dependencies (stdlib `fcntl`, POSIX-only).
