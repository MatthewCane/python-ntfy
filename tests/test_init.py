from os import environ

from python_ntfy import NtfyClient

from .helpers import topic


def test_init_no_auth(localhost_server_no_auth, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    assert ntfy._server == environ["NTFY_SERVER"]
    assert ntfy._auth == ("", "")
    assert ntfy._topic == topic


def test_init_with_auth_env(localhost_server_auth, user_pass_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    assert ntfy._server == environ.get("NTFY_SERVER")
    assert ntfy._auth == (environ["NTFY_USER"], environ["NTFY_PASSWORD"])
    assert ntfy._topic == topic


def test_init_set_topic(localhost_server_no_auth, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    assert ntfy._topic == topic
    assert ntfy.url == "/".join([environ["NTFY_SERVER"], topic])
    # Reset the topic
    ntfy.set_topic("test2")
    assert ntfy._topic == "test2"
    assert ntfy.url == "/".join([environ["NTFY_SERVER"], "test2"])
    assert ntfy.get_topic() == "test2"


def test_init_no_server(no_server, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    assert ntfy._server == "https://ntfy.sh"
