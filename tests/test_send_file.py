from datetime import datetime
from time import sleep

import requests
from pytest import raises

from python_ntfy import MessageSendError, NtfyClient

from .helpers import topic


def test_send_text_file(localhost_server_no_auth, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send_file("tests/assets/test_text.txt")
    assert response["attachment"]["name"] == "test_text.txt"
    assert response["attachment"]["type"] == "text/plain; charset=utf-8"


def test_send_image_file(localhost_server_no_auth, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send_file("tests/assets/test_image.png")
    assert response["attachment"]["name"] == "test_image.png"
    assert response["attachment"]["type"] == "image/png"


def test_send_scheduled_file(localhost_server_no_auth, no_auth) -> None:
    ts = datetime.fromtimestamp(int(datetime.now().timestamp()) + 10)
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send_file("tests/assets/test_text.txt", schedule=ts)
    assert response["attachment"]["name"] == "test_text.txt"
    assert response["attachment"]["type"] == "text/plain; charset=utf-8"
    assert response["time"] == int(ts.timestamp())


def test_send_file_with_email(localhost_server_no_auth, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send_file("tests/assets/test_text.txt", email="test@test.com")
    print(response)
    assert response["attachment"]["name"] == "test_text.txt"
    assert response["attachment"]["type"] == "text/plain; charset=utf-8"

    sleep(1)

    res = requests.get(
        "http://localhost:8082/api/v1/messages", timeout=10
    ).content.decode()
    print(res)
    assert "test_text.txt" in res


def test_send_file_not_found() -> None:
    ntfy = NtfyClient(topic=topic)
    with raises(MessageSendError):
        ntfy.send_file(file="not_found.txt")
