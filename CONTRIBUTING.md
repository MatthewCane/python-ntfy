# Contributing to python-ntfy

We welcome contributions. This guide explains how to set up your environment, follow the project’s conventions, and submit high‑quality changes. You are welcome to use AI tools for assistance, but any code or documentation submitted must be thoroughly reviewed and verified by a human before opening a pull request.

## What you can work on

- Features and bug fixes in `python_ntfy`
- Documentation under `docs/`
- Tests under `tests/`
- Examples and developer experience improvements

## Prerequisites

Install these tools before contributing:

- uv: Fast Python package manager and builder — see `https://github.com/astral-sh/uv`
- Just: Task runner used for common workflows — see `https://github.com/casey/just`
- Docker and Docker Compose: Required to run integration tests locally
- Pre-commit: Optional but recommended for local quality checks — see `https://pre-commit.com/`

Supported Python versions: 3.12 and 3.13 (see `pyproject.toml`).

## Local setup

- Fork the repository and create a feature branch
- Run `just setup` to install hooks and sync dev deps
- Make your changes
- Run `just format` to auto-format and fix common issues
- Run `just test` to execute linters, type checks, and tests

Useful tasks (see `Justfile`):

- `just check` — Ruff lint and format checks
- `just mypy` — Type checking
- `just pytest` — Run tests
- `just build-docs` / `just serve-docs` — Build/serve docs

Tests use Docker containers defined in `tests/assets/test_containers.yml` and are orchestrated automatically by fixtures in `tests/conftest.py`.

## Coding standards

- Style and linting: Ruff (rules configured in `pyproject.toml`)
- Typing: mypy: public modules are held to stricter settings (see `tool.mypy.overrides`)
- Target Python: 3.12 (`tool.ruff.target-version`)
- Keep code readable with clear names and guard clauses; prefer explicitness
- Update or add tests for new behavior; keep coverage at or above enforced threshold

## Commit messages

- Be concise and descriptive
- Use imperative mood (e.g., "Add support for X")

## Pull requests

- Include a clear summary: problem, solution, and alternatives considered
- Add tests and documentation updates where applicable
- Ensure `just test` passes locally
- Keep PRs focused and reasonably sized
- Link related issues, if any

## Security and licensing

- Do not commit API keys, passwords, tokens, or other secrets
- Do not copy code you are not licensed to contribute under the project’s MIT license

## AI assistance policy

- You may use AI tools to help write or refactor code and docs
- All changes must be thoroughly reviewed and verified by a human contributor before opening a PR
- The submitter is responsible for correctness and licensing

## Getting help

- Open an issue with questions or proposals
- Mention maintainers in issues/PRs as needed

Thank you for contributing to python-ntfy! 🚀
