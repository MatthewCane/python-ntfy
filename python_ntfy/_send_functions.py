import json
import requests
from enum import Enum
from typing import Optional, Union


class MessagePriority(Enum):
    """
    Ntfy message priority levels.
    """

    MIN = "1"
    LOW = "2"
    DEFAULT = "3"
    HIGH = "4"
    MAX = "5"
    URGENT = MAX


class ActionType(Enum):
    """
    Action button types
    """

    VIEW = "view"
    BROADCAST = "broadcast"
    HTTP = "http"


class Action:
    def __init__(self, label: str, url: str, clear: bool = False):
        self.label = label
        self.url = url
        self.actions: list = []
        self.clear = clear


class ViewAction(Action):
    def __init__(self, label: str, url: str, clear: bool = False):
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
    def __init__(
        self,
        label: str,
        intent: str = "io.heckel.ntfy.USER_ACTION",
        extras: Optional[dict] = None,
        clear: bool = False,
    ):
        self.action = ActionType.BROADCAST
        self.intent = intent
        self.extras = extras
        super().__init__(label, ActionType.BROADCAST, clear)

    def to_dict(self) -> dict:
        return {
            "action": self.action.value,
            "label": self.label,
            "extras": self.extras,
            "clear": self.clear,
        }

    def to_header(self) -> str:
        extras = ""
        if self.extras is not None:
            for key, value in self.extras.items():
                extras += f"{key}={value},"
        return f"action={self.action.value}, label={self.label}, url={self.url}, clear={self.clear}"


class HttpAction(Action):
    def __init__(
        self,
        label: str,
        url: str,
        method: str = "POST",
        headers: Optional[dict] = None,
        body: Optional[str] = None,
        clear: bool = False,
    ):
        self.action = ActionType.HTTP
        self.method = method
        self.headers = headers
        self.body = body
        super().__init__(label, url, clear)

    def to_dict(self) -> dict:
        action_dict = {
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
    title: str = None,
    priority: Optional[MessagePriority] = MessagePriority.DEFAULT,
    tags: list = [],
    actions: list[Union[ViewAction, BroadcastAction, HttpAction, None]] = [],
    format_as_markdown: bool = False,
) -> dict:
    """
    Send a text based message to the server

    :param message: The message to send
    :param title: The title of the message. Optional
    :param priority: The priority of the message. Optional, defaults to MessagePriority.DEFAULT
    :param tags: A list of tags to attach to the message. Can be an emoji short code. Optional
    :param format_as_markdown: If true, the message will be formatted as markdown. Optional
    :param actions: A list of Actions objects to attach to the message. Optional
    :return: The response from the server

    :examples:
    response = client.send(message="Example message")
    response = client.send(message="Example message", title="Example title", priority=MessagePriority.HIGH, tags=["fire", "warning"])
    response = client.send(message="*Example markdown*", format_as_markdown=True)
    """
    headers = {
        "Title": title,
        "Priority": priority.value,
        "Tags": ",".join(tags),
        "Markdown": "true" if format_as_markdown else "false",
    }
    if len(actions) > 0:
        headers["Actions"] = " ; ".join([action.to_header() for action in actions])

    response = json.loads(
        requests.post(url=self.url, data=message, headers=headers, auth=self._auth).text
    )
    return response


def send_file(
    self,
    file: str,
    title: str = None,
    priority: Optional[MessagePriority] = MessagePriority.DEFAULT,
    tags: list = [],
    actions: list[Union[ViewAction, BroadcastAction, HttpAction, None]] = [],
) -> dict:
    """
    Send a file to the server

    :param file_path: The path to the file to send.
    :param title: The title of the file. Optional
    :param priority: The priority of the message. Optional, defaults to MessagePriority.DEFAULT
    :param tags: A list of tags to attach to the message. Can be an emoji short code. Optional
    :param actions: A list of ActionButton objects to attach to the message. Optional
    :return: The response from the server

    :examples:
    response = client.send_file(file_path="example.txt")
    """
    headers = {
        "Title": title,
        "Filename": file.split("/")[-1],
        "Priority": priority.value,
        "Tags": ",".join(tags),
        "Actions": " ; ".join([action.to_header() for action in actions]),
    }

    with open(file, "rb") as file:
        response = json.loads(
            requests.post(
                url=self.url, data=file, headers=headers, auth=self._auth
            ).text
        )
    return response
