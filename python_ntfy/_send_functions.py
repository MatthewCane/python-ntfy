import json
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional, Union

import requests


class MessagePriority(Enum):
    """Ntfy message priority levels.

    Attributes:
        MIN: The minimum priority.
        LOW: A low priority.
        DEFAULT: The default priority.
        HIGH: A high priority.
        MAX: The maximum priority.
        URGENT: The maximum priority.
    """

    MIN = "1"
    LOW = "2"
    DEFAULT = "3"
    HIGH = "4"
    MAX = "5"
    URGENT = MAX


class ActionType(Enum):
    """Action button types.

    Attributes:
        VIEW: A view action button.
        BROADCAST: A broadcast action button.
        HTTP: An HTTP action button.
    """

    VIEW = "view"
    BROADCAST = "broadcast"
    HTTP = "http"


class Action:
    def __init__(self, label: str, url: str, clear: bool = False) -> None:
        self.label = label
        self.url = url
        self.actions: list = []
        self.clear = clear


class ViewAction(Action):
    """A view action button.

    The view action opens a website or app when the action button is tapped.
    """

    def __init__(self, label: str, url: str, clear: bool = False) -> None:
        """Initialize a ViewAction.

        Args:
            label: Label of the action button in the notification.
            url: URL to open when action is tapped.
            clear: Clear notification after action button is tapped.
        """
        self.action = ActionType.VIEW
        super().__init__(label=label, url=url, clear=clear)

    def to_dict(self) -> dict:
        return {
            "action": self.action.value,
            "label": self.label,
            "url": self.url,
            "clear": self.clear,
        }

    def to_header(self) -> str:
        return f"action={self.action.value}, label={self.label}, url={self.url}, clear={self.clear}"


class BroadcastAction(Action):
    """A broadcast action button.

    The broadcast action sends an Android broadcast intent when the action button is tapped.
    """

    def __init__(
        self,
        label: str,
        intent: str = "io.heckel.ntfy.USER_ACTION",
        extras: Optional[dict[str, str]] = None,
        clear: bool = False,
    ) -> None:
        """Initialize a BroadcastAction.

        Args:
            label: Label of the action button in the notification.
            intent: Android intent name.
            extras: Android intent extras.
            clear: Clear notification after action button is tapped.
        """
        self.action = ActionType.BROADCAST
        self.intent = intent
        self.extras = extras
        super().__init__(label, ActionType.BROADCAST.value, clear)

    def to_dict(self) -> dict:
        return {
            "action": self.action.value,
            "label": self.label,
            "extras": self.extras,
            "clear": self.clear,
            "intent": self.intent,
        }

    def to_header(self) -> str:
        if self.extras:
            extras_str = ", ".join([f"extras.{k}={v}" for k, v in self.extras.items()])
        return (
            f"action={self.action.value}, label={self.label}, url={self.url}, clear={self.clear}, intent={self.intent}"
            + extras_str
            if self.extras
            else ""
        )


class HttpAction(Action):
    """An HTTP action button.

    The http action sends a HTTP request when the action button is tapped.
    """

    def __init__(
        self,
        label: str,
        url: str,
        method: str = "POST",
        headers: Optional[dict[str, str]] = None,
        body: Optional[str] = None,
        clear: bool = False,
    ) -> None:
        """Initialize an HttpAction.

        Args:
            label: Label of the action button in the notification.
            url: URL to open when action is tapped.
            method: HTTP method to use for request.
            headers: HTTP headers to send with the request.
            body: HTTP body to send with the request.
            clear: Clear notification after HTTP request succeeds. If the request fails, the notification is not cleared.
        """
        self.action = ActionType.HTTP
        self.method = method
        self.headers = headers
        self.body = body
        super().__init__(label, url, clear)

    def to_dict(self) -> dict[str, Union[str, bool, dict[str, str]]]:
        action_dict: dict[str, Union[str, bool, dict[str, str]]] = {
            "action": self.action.value,
            "label": self.label,
            "url": self.url,
            "method": self.method,
            "clear": self.clear,
        }
        if self.headers:
            action_dict["headers"] = self.headers
        if self.body:
            action_dict["body"] = self.body
        return action_dict

    def to_header(self) -> str:
        header_str = f"action={self.action.value}, label={self.label}, url={self.url}, method={self.method}, clear={self.clear}"
        if self.headers is not None:
            headers = ""
            for key, value in self.headers.items():
                headers += f"headers.{key}={value}"
            header_str += f", {headers}"
        if self.body:
            header_str += f", body={self.body}"
        print(header_str)
        return header_str


def send(
    self,
    message: str,
    title: Optional[str] = None,
    priority: MessagePriority = MessagePriority.DEFAULT,
    tags: Optional[list] = None,
    actions: Optional[list[Union[ViewAction, BroadcastAction, HttpAction]]] = None,
    schedule: Optional[datetime] = None,
    format_as_markdown: bool = False,
    timeout_seconds: int = 5,
    email: Optional[str] = None,
) -> dict:
    """Send a text-based message to the server.

    Call this function to send a message to the server. The message will be sent
    to the server and then broadcast to all clients subscribed to the topic.

    Args:
        message: The message to send.
        title: The title of the message.
        priority: The priority of the message.
        tags: A list of tags to attach to the message. Can be an emoji short code.
        actions: A list of Actions objects to attach to the message.
        schedule: The time to schedule the message to be sent.
        format_as_markdown: If true, the message will be formatted as markdown.
        additional_topics: A list of additional topics to send the message to.
        timeout_seconds: The number of seconds to wait before timing out the reqest to the server.
        email: Forward messages to an email address. Only one email address can be specified.

    Returns:
        dict: The response from the server.

    Raises:
        ToDo

    Examples:
        >>> response = client.send(message="Example message")

        >>> response = client.send(message="Example message", title="Example title", priority=MessagePriority.HIGH, tags=["fire", "warning"])

        >>> response = client.send(message="*Example markdown*", format_as_markdown=True)
    """
    if tags is None:
        tags = []
    if actions is None:
        actions = []

    headers = {
        "Title": title,
        "Priority": priority.value,
        "Tags": ",".join(tags),
        "Markdown": str(format_as_markdown).lower(),
    }
    if len(actions) > 0:
        headers["Actions"] = " ; ".join([action.to_header() for action in actions])

    if email:
        headers["Email"] = email

    if schedule:
        headers["Delay"] = str(int(schedule.timestamp()))

    return json.loads(
        requests.post(
            url=self.url,
            data=message,
            headers=headers,
            auth=self._auth,
            timeout=timeout_seconds,
        ).text,
    )


def send_file(
    self,
    file: str,
    title: Optional[str] = None,
    priority: MessagePriority = MessagePriority.DEFAULT,
    tags: Optional[list] = None,
    actions: Optional[list[Union[ViewAction, BroadcastAction, HttpAction]]] = None,
    schedule: Optional[datetime] = None,
    timeout_seconds: int = 30,
    email: Optional[str] = None,
) -> dict:
    """Sends a file to the server.

    Args:
        file: The path to the file to send.
        title: The title of the file.
        priority: The priority of the message. Optional, defaults to MessagePriority.
        tags: A list of tags to attach to the message. Can be an emoji short code.
        actions: A list of ActionButton objects to attach to the message.
        schedule: The time to schedule the message to be sent. Must be more than 10 seconds away and less than 3 days in the future.
        timeout_seconds: The number of seconds to wait before timing out.
        email: Forward messages to an email address. Only one email address can be specified.

    Returns:
        dict: The response from the server.

    Raises:
        ToDo

    Examples:
        >>> response = client.send_file(file="example.txt")
    """
    if actions is None:
        actions = []
    if tags is None:
        tags = []

    headers = {
        "Title": str(title),
        "Filename": file.split("/")[-1],
        "Priority": priority.value,
        "Tags": ",".join(tags),
        "Actions": " ; ".join([action.to_header() for action in actions]),
    }

    if email:
        headers["Email"] = email

    if schedule:
        headers["Delay"] = str(int(schedule.timestamp()))

    with Path(file).open("rb") as f:
        return json.loads(
            requests.post(
                url=self.url,
                data=f,
                headers=headers,
                auth=self._auth,
                timeout=timeout_seconds,
            ).text,
        )
