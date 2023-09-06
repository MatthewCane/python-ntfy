from python_ntfy import NtfyClient
import dotenv
from .helpers import *


def test_send_without_auth():
    clear_env()
    topic = get_topic()
    ntfy = NtfyClient(
        topic=topic,
    )
    response = ntfy.send(message="test_send_without_auth")
    print(response)
    assert response["error"] == "unauthorized"


def test_send_with_auth_env():
    topic = get_topic()
    dotenv.load_dotenv()
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(message="test_send_with_auth_env")
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic


def test_send_with_markdown():
    topic = get_topic()
    dotenv.load_dotenv()
    with open("tests/assets/test_markdown.md", "r") as f:
        message = f.read()
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(format_as_markdown=True, message=message)
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic
    assert response["content_type"] == "text/markdown"


def test_send_with_title():
    topic = get_topic()
    dotenv.load_dotenv()
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(message="test_send_with_title", title="Test Title")
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic
    assert response["title"] == "Test Title"
