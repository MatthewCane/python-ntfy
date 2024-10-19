from python_ntfy import NtfyClient

from .helpers import topic


def test_view_action() -> None:
    ntfy = NtfyClient(topic=topic)
    action = ntfy.ViewAction(label="View", url="https://ntfy.sh").to_dict()
    assert action["action"] == "view"
    assert action["label"] == "View"
    assert action["url"] == "https://ntfy.sh"


def test_broadcast_action() -> None:
    ntfy = NtfyClient(topic=topic)
    action = ntfy.BroadcastAction(
        label="Broadcast",
        intent="com.example.broadcast",
    ).to_dict()
    assert action["action"] == "broadcast"
    assert action["label"] == "Broadcast"
    assert action["intent"] == "com.example.broadcast"


def test_http_action() -> None:
    ntfy = NtfyClient(topic=topic)
    action = ntfy.HttpAction(
        label="HTTP",
        url="https://ntfy.sh",
        method="POST",
    ).to_dict()
    assert action["action"] == "http"
    assert action["label"] == "HTTP"
    assert action["url"] == "https://ntfy.sh"
    assert action["method"] == "POST"
