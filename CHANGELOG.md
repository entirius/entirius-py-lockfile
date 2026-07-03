# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-07-03

Initial public release.

### Added

- `LockFile` — file-based lock via `fcntl.flock`, atomic across forked processes;
  non-blocking `acquire()` by default or blocking with `wait_for_acquire=True`.
- Toolchain: uv (env + lock), ruff (lint + format), hatchling (build), pytest;
  MPL-2.0 with per-file headers; pre-commit + CI (lint, test, secret-scan).
