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

# Run python tests
[group("tests")]
pytest:
    docker info > /dev/null 2>&1 || echo "Error: Docker must be running to run pytest" && exit 1
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
    echo "> Running ruff format..."
    uv run ruff format
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

# Bump version and create draft release
[confirm("Are you sure you want to create a draft release? [y/N]")]
[group("release")]
draft-release bump='patch':
    #!/bin/bash
    git pull origin main
    @just build
    VERSION=$(uv version --bump {{ bump }} --short)
    echo "> Bumping version to $VERSION"
    git reset
    git add pyproject.toml uv.lock
    git commit -m "Bump version to $VERSION"
    git push origin main
    gh release create $VERSION dist/python_ntfy* --draft --generate-notes
    echo "> Follow the link to review and publish the release"
