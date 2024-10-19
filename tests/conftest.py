from pytest import fixture


@fixture
def localhost_server(monkeypatch) -> None:
    monkeypatch.setenv("NTFY_SERVER", "http://localhost")


@fixture
def ntfy_sh_server(monkeypatch) -> None:
    monkeypatch.setenv("NTFY_SERVER", "https://ntfy.sh")


@fixture
def user_pass_auth(monkeypatch) -> None:
    monkeypatch.delenv("NTFY_TOKEN", raising=False)
    monkeypatch.setenv("NTFY_USER", "example_user")
    monkeypatch.setenv("NTFY_PASSWORD", "example_password")


@fixture
def token_auth(monkeypatch) -> None:
    # This is a dummy token, not valid
    monkeypatch.delenv("NTFY_USER", raising=False)
    monkeypatch.delenv("NTFY_PASSWORD", raising=False)
    monkeypatch.setenv("NTFY_TOKEN", "tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2")


@fixture
def no_auth(monkeypatch) -> None:
    monkeypatch.delenv("NTFY_USER", raising=False)
    monkeypatch.delenv("NTFY_PASSWORD", raising=False)
    monkeypatch.delenv("NTFY_USER", raising=False)
