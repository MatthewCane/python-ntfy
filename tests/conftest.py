import subprocess
from pathlib import Path
from time import sleep
from typing import Generator

from pytest import fixture, mark


@fixture
def localhost_server_no_auth(monkeypatch) -> None:
    monkeypatch.setenv("NTFY_SERVER", "http://localhost:8080")


@fixture
def localhost_server_auth(monkeypatch) -> None:
    monkeypatch.setenv("NTFY_SERVER", "http://localhost:8081")


@fixture
def user_pass_auth(monkeypatch) -> None:
    monkeypatch.delenv("NTFY_TOKEN", raising=False)
    monkeypatch.setenv("NTFY_USER", "test-admin")
    monkeypatch.setenv("NTFY_PASSWORD", "test-admin")


@fixture
def token_auth(monkeypatch) -> None:
    monkeypatch.delenv("NTFY_USER", raising=False)
    monkeypatch.delenv("NTFY_PASSWORD", raising=False)
    monkeypatch.setenv("NTFY_TOKEN", "tk_vylbjn9dp5vultzin5qin6weuzd4w")


@fixture
def no_auth(monkeypatch) -> None:
    monkeypatch.delenv("NTFY_USER", raising=False)
    monkeypatch.delenv("NTFY_PASSWORD", raising=False)
    monkeypatch.delenv("NTFY_USER", raising=False)


@fixture(scope="session", autouse=True)
def docker_compose_up() -> Generator:
    """Fixture to start up docker compose before tests and tear it down after."""
    compose_file = Path("tests/assets/test_containers.yml").resolve()

    # Start up docker compose
    subprocess.run(  # noqa: S603
        ["docker-compose", "-f", str(compose_file), "up", "-d"],  # noqa: S607
        check=True,
        capture_output=True,
    )

    sleep(0.5)

    # Run the tests
    yield

    # Tear down the containers
    subprocess.run(["docker-compose", "-f", str(compose_file), "down"], check=True)  # noqa: S607, S603


def pytest_configure(config) -> None:
    config.addinivalue_line(
        "markers", "requires_docker: mark test as requiring docker services"
    )


def pytest_collection_modifyitems(session, config, items) -> None:
    """Automatically mark all test items as requiring docker."""
    for item in items:
        item.add_marker(mark.requires_docker)
