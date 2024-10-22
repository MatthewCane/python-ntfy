from os import environ
from pathlib import Path

from python_ntfy import NtfyClient

from .helpers import topic


def test_send_without_auth_error(localhost_server_auth, no_auth) -> None:
    # This should fail and return an unauthorized error
    ntfy = NtfyClient(
        topic=topic,
    )
    response = ntfy.send(message="test_send_without_auth")
    print(response)
    assert response["error"] == "unauthorized"


def test_send_without_auth(localhost_server_no_auth, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(message="test_send_without_auth")
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic


def test_send_with_auth(localhost_server_auth, user_pass_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(message="test_send_with_auth_env")
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic


def test_send_with_auth_token(localhost_server_auth, token_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(message="test_send_with_auth_token")
    print(response)
    assert ntfy._auth == ("", environ["NTFY_TOKEN"])
    assert response["event"] == "message"
    assert response["topic"] == topic


def test_send_with_markdown(localhost_server_no_auth, no_auth) -> None:
    with Path("tests/assets/test_markdown.md").open() as f:
        message = f.read()
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(format_as_markdown=True, message=message)
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic
    assert response["content_type"] == "text/markdown"


def test_send_with_title(localhost_server_no_auth, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(message="test_send_with_title", title="Test Title")
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic
    assert response["title"] == "Test Title"


def test_send_with_tags(localhost_server_no_auth, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(message="test_send_with_tags", tags=["fire", "warning"])
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic
    assert response["tags"] == ["fire", "warning"]


def test_send_with_priority(localhost_server_no_auth, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(
        message="test_send_with_priority",
        priority=ntfy.MessagePriority.HIGH,
    )
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic
    assert response["priority"] == 4


def test_send_with_view_action(localhost_server_no_auth, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(
        message="test_send_with_view_action",
        actions=[
            ntfy.ViewAction(label="View", url="https://ntfy.sh"),
        ],
    )
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic
    assert response["actions"] is not None


def test_send_with_broadcast_action(localhost_server_no_auth, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(
        message="test_send_with_broadcast_action",
        actions=[
            ntfy.BroadcastAction(label="Broadcast", extras={"test": "test"}),
        ],
    )
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic
    assert response["actions"] is not None


def test_send_with_http_action(localhost_server_no_auth, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(
        message="test_send_with_http_action",
        actions=[
            ntfy.HttpAction(
                label="HTTP",
                url="https://posttestserver.dev/p/pythonntfy/post",
                headers={"Content-Type": "application/json"},
                body='{"test": "test"}',
            ),
        ],
    )
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic
    assert response["actions"] is not None
