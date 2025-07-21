from datetime import datetime

from python_ntfy import NtfyClient

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
