from python_ntfy import NtfyClient

from .helpers import topic


def test_send_text_file(localhost_server, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send_file("tests/assets/test_text.txt")
    assert response["attachment"]["name"] == "test_text.txt"
    assert response["attachment"]["type"] == "text/plain; charset=utf-8"


def test_send_image_file(localhost_server, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send_file("tests/assets/test_image.png")
    assert response["attachment"]["name"] == "test_image.png"
    assert response["attachment"]["type"] == "image/png"
