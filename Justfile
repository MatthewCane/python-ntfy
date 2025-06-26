set quiet := true

# Show all recipes
help:
  @just --list --unsorted

# Run python tests
pytest:
  echo "> Running python tests..."
  poetry run pytest -v --cov=python_ntfy --cov-fail-under=95

# Run ruff checks
check:
  echo "> Running ruff code quality check..."
  poetry run ruff check
  echo "> Running ruff format check..."
  poetry run ruff format --check

# Run mypy type checks
mypy:
  echo "> Running mypy checks..."
  poetry run mypy .

# Run all tests
test: check mypy pytest

# Run ruff format
format:
  echo "> Running ruff format..."
  poetry run ruff format

# Install dependencies
install:
  echo "> Installing dependencies..."
  poetry install --with dev

# Build mkdocs site
build-docs:
  echo "> Building docs..."
  poetry run mkdocs build

# Serve mkdocs site and watch for changes
serve-docs: build-docs
  echo "> Serving docs..."
  poetry run mkdocs serve
