from datetime import datetime
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
    assert response["error"] == "forbidden"


def test_send_without_auth(localhost_server_no_auth, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(message="test_send_without_auth")
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic


def test_send_with_auth_env(localhost_server_auth, user_pass_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(message="test_send_with_auth_env")
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic


def test_send_with_auth_token_env(localhost_server_auth, token_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(message="test_send_with_auth_token")
    print(response)
    assert ntfy._auth == ("", environ["NTFY_TOKEN"])
    assert response["event"] == "message"
    assert response["topic"] == topic


def test_send_with_auth_args(localhost_server_auth, user_pass_auth) -> None:
    auth = (environ["NTFY_USER"], environ["NTFY_PASSWORD"])
    ntfy = NtfyClient(topic=topic, auth=auth)
    response = ntfy.send(message="test_send_with_auth_args")
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic


def test_send_with_auth_token_args(localhost_server_auth, token_auth) -> None:
    auth = environ["NTFY_TOKEN"]
    ntfy = NtfyClient(topic=topic, auth=auth)
    response = ntfy.send(message="test_send_with_auth_token_args")
    print(response)
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


def test_send_scheduled_message(localhost_server_no_auth, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    ts = datetime.fromtimestamp(int(datetime.now().timestamp()) + 10)
    response = ntfy.send(message="test_send_scheduled_message", schedule=ts)
    print(ts, response)
    assert response["event"] == "message"
    assert response["topic"] == topic
    assert response["time"] == int(ts.timestamp())


def test_send_message_without_auth(no_server, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(message="test_send_message_without_auth")
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic


def test_send_message_with_email(localhost_server_no_auth, no_auth) -> None:
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(message="test_send_message_with_email", email="test@test.com")
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic
