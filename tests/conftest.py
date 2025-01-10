import subprocess
from collections.abc import Generator
from json import loads
from pathlib import Path
from time import sleep

from pytest import fixture, mark
from requests import get


@fixture
def localhost_server_no_auth(monkeypatch) -> None:
    monkeypatch.setenv("NTFY_SERVER", "http://localhost:8080")


@fixture
def localhost_server_auth(monkeypatch) -> None:
    monkeypatch.setenv("NTFY_SERVER", "http://localhost:8081")


@fixture
def no_server(monkeypatch) -> None:
    monkeypatch.delenv("NTFY_SERVER", raising=False)


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


def get_container_status(port: int) -> bool:
    try:
        return loads(get(f"http://localhost:{port}/v1/health", timeout=1).content)[
            "healthy"
        ]
    except ConnectionError:
        return False


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

    # Check that the containers are ready
    max_retries = 10
    sleep_time = 0.5
    for _ in range(max_retries):
        if get_container_status(8080) and get_container_status(8081):
            break
        sleep(sleep_time)
    else:
        msg = f"Test containers did not start after {int(max_retries * sleep_time)} seconds."
        raise TimeoutError(msg)

    # Run the tests
    yield

    # Tear down the containers
    subprocess.run(["docker-compose", "-f", str(compose_file), "down"], check=True)  # noqa: S607, S603


def pytest_configure(config) -> None:
    """Add the requires_docker marker to pytest."""
    config.addinivalue_line(
        "markers", "requires_docker: mark test as requiring docker services"
    )


def pytest_collection_modifyitems(session, config, items) -> None:
    """Automatically mark all test items as requiring docker."""
    for item in items:
        item.add_marker(mark.requires_docker)
