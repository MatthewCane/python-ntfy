from python_ntfy import NtfyClient
import os, dotenv
from .helpers import *


def test_init_no_auth():
    clear_env()
    ntfy = NtfyClient(topic="test")
    assert ntfy._server == "https://ntfy.sh"
    assert ntfy._auth == ("", "")
    assert ntfy._topic == "test"


def test_init_with_auth_env():
    dotenv.load_dotenv()
    ntfy = NtfyClient(topic="test")
    assert ntfy._server == "https://ntfy.sh"
    assert ntfy._auth == (os.environ["NTFY_USER"], os.environ["NTFY_PASSWORD"])
    assert ntfy._topic == "test"


def test_init_set_topic():
    ntfy = NtfyClient(topic="test")
    assert ntfy._topic == "test"
    assert ntfy.url == "https://ntfy.sh/test"
    ntfy.set_topic("test2")
    assert ntfy._topic == "test2"
    assert ntfy.url == "https://ntfy.sh/test2"
