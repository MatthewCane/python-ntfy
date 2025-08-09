set quiet := true

# Show all recipes
help:
    @just --list --unsorted

# Clean up all untracked files (including those in .gitignore)
[group("housekeeping")]
clean:
    echo "> Cleaning up all untracked files..."
    git clean -fdx

# Set up and validate development dependencies
[group("housekeeping")]
setup:
    echo "> Installing pre-commit hooks..."
    pre-commit install
    uv sync --dev

# Run python tests. Docker is required to run the tests.
[group("tests")]
pytest:
    echo "> Running python tests..."
    uv run pytest -v

# Run ruff checks
[group("tests")]
check:
    echo "> Running ruff code quality check..."
    uv run ruff check
    echo "> Running ruff format check..."
    uv run ruff format --check

# Run mypy type checks
[group("tests")]
mypy:
    echo "> Running mypy checks..."
    uv run mypy python_ntfy

# Run ruff format
[group("tests")]
format:
    echo "> Running ruff formater and fixer..."
    uv run ruff format
    uv run ruff check --fix
    echo "> Running just format..."
    just --fmt --unstable

# Run all tests
[group("tests")]
test: check mypy pytest

# Build mkdocs site
[group("docs")]
build-docs:
    echo "> Building docs..."
    uv run mkdocs build

# Serve mkdocs site and watch for changes
[group("docs")]
serve-docs: build-docs
    echo "> Serving docs..."
    uv run mkdocs serve

# Build the package
[group("release")]
build:
    rm -rf dist
    echo "> Building package..."
    uv build

# Bump version, push and create draft release
[confirm("Are you sure you want to draft a release? [y/N]")]
[group("release")]
draft-release bump='patch':
    @just _bump_version {{ bump }}
    @just _push_version
    @just _create_draft_release

_bump_version bump:
    git checkout main
    git pull origin main
    git reset # Unstage all files
    @just build
    uv version --bump {{ bump }}
    git add pyproject.toml uv.lock

[confirm("Are you sure you want to push the version change? [y/N]")]
_push_version:
    git commit -m "Bumped version to $(uv version --short)"
    git push origin main

_create_draft_release:
    gh release create $(uv version --short) dist/python_ntfy* --draft --generate-notes
    echo "> Follow the link to review and publish the release"
