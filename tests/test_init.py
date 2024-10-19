import os

from python_ntfy import NtfyClient

from .helpers import topic


def test_init_no_auth(localhost_server, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    assert ntfy._server == os.environ.get("NTFY_SERVER") or "https://ntfy.sh"
    assert ntfy._auth == ("", "")
    assert ntfy._topic == topic


def test_init_with_auth_env(localhost_server, user_pass_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    assert ntfy._server == os.environ.get("NTFY_SERVER") or "https://ntfy.sh"
    assert ntfy._auth == (os.environ["NTFY_USER"], os.environ["NTFY_PASSWORD"])
    assert ntfy._topic == topic


def test_init_set_topic(localhost_server, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    assert ntfy._topic == topic
    assert (
        ntfy.url == "/".join([os.environ["NTFY_SERVER"], "test"])
        or "https://ntfy.sh/test"
    )
    ntfy.set_topic("test2")
    assert ntfy._topic == "test2"
    assert (
        ntfy.url == "/".join([os.environ["NTFY_SERVER"], "test2"])
        or "https://ntfy.sh/test2"
    )
