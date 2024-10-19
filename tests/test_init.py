import os

import dotenv

from python_ntfy import NtfyClient

from .helpers import clear_env


def test_init_no_auth() -> None:
    clear_env()
    ntfy = NtfyClient(topic="test")
    assert ntfy._server == os.environ.get("NTFY_SERVER") or "https://ntfy.sh"
    assert ntfy._auth == ("", "")
    assert ntfy._topic == "test"


def test_init_with_auth_env() -> None:
    dotenv.load_dotenv()
    ntfy = NtfyClient(topic="test")
    assert ntfy._server == os.environ.get("NTFY_SERVER") or "https://ntfy.sh"
    assert ntfy._auth == (os.environ["NTFY_USER"], os.environ["NTFY_PASSWORD"])
    assert ntfy._topic == "test"


def test_init_set_topic() -> None:
    ntfy = NtfyClient(topic="test")
    assert ntfy._topic == "test"
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
