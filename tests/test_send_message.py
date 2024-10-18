from python_ntfy import NtfyClient
import dotenv
from .helpers import clear_env, get_topic
from pytest import MonkeyPatch


def test_send_without_auth_ntfysh():
    clear_env()
    topic = get_topic()
    ntfy = NtfyClient(
        topic=topic,
    )
    response = ntfy.send(message="test_send_without_auth")
    print(response)
    assert response["error"] == "unauthorized"


def test_send_without_auth_selfhosted_no_auth():
    dotenv.load_dotenv()
    clear_env(server=False)
    topic = get_topic()
    ntfy = NtfyClient(topic=topic)
    # Skip this test if testing against ntfy.sh
    # as it requires auth
    if ntfy._server == "https://ntfy.sh":
        return
    response = ntfy.send(message="test_send_without_auth")
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic


def test_send_with_auth_env():
    topic = get_topic()
    dotenv.load_dotenv()
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(message="test_send_with_auth_env")
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic


def test_send_with_auth_token():
    topic = get_topic()
    dotenv.load_dotenv()
    with MonkeyPatch().context() as m:
        m.delenv("NTFY_USER", raising=False)
        m.delenv("NTFY_PASSWORD", raising=False)
        # This is a dummy token, not valid
        m.setenv("NTFY_TOKEN", "tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2")
        ntfy = NtfyClient(topic=topic)
        response = ntfy.send(message="test_send_with_auth_token")
        print(response)
        assert ntfy._auth == ("", "tk_AgQdq7mVBoFD37zQVN29RhuMzNIz2")
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


def test_send_with_tags():
    topic = get_topic()
    dotenv.load_dotenv()
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(message="test_send_with_tags", tags=["fire", "warning"])
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic
    assert response["tags"] == ["fire", "warning"]


def test_send_with_priority():
    topic = get_topic()
    dotenv.load_dotenv()
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(
        message="test_send_with_priority", priority=ntfy.MessagePriority.HIGH
    )
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic
    assert response["priority"] == 4


def test_send_with_view_action():
    topic = get_topic()
    dotenv.load_dotenv()
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


def test_send_with_broadcast_action():
    topic = get_topic()
    dotenv.load_dotenv()
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


def test_send_with_http_action():
    topic = get_topic()
    dotenv.load_dotenv()
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(
        message="test_send_with_http_action",
        actions=[
            ntfy.HttpAction(
                label="HTTP",
                url="https://posttestserver.dev/p/pythonntfy/post",
                headers={"Content-Type": "application/json"},
                body='{"test": "test"}',
            )
        ],
    )
    print(response)
    assert response["event"] == "message"
    assert response["topic"] == topic
    assert response["actions"] is not None
