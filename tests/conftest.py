from pytest import fixture


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
