"""This module provides the NtfyClient class for interacting with the ntfy notification service.

The NtfyClient class allows users to send notifications, files, and perform various actions
through the ntfy.sh service. It also supports retrieving cached messages.

Typical usage example:

    client = NtfyClient(topic="my_topic")
    client.send("Hello, World!")
"""

import os

from ._get_functions import get_cached_messages
from ._send_functions import (
    BroadcastAction,
    HttpAction,
    MessagePriority,
    ViewAction,
    send,
    send_file,
)


class GetFunctionsMixin:
    """Mixin for getting messages."""

    get_cached_messages = get_cached_messages


class SendFunctionsMixin:
    """Mixin for sending messages."""

    send = send
    send_file = send_file
    BroadcastAction = BroadcastAction
    HttpAction = HttpAction
    MessagePriority = MessagePriority
    ViewAction = ViewAction


class NtfyClient(GetFunctionsMixin, SendFunctionsMixin):
    """A class for interacting with the ntfy notification service."""

    def __init__(
        self,
        topic: str,
        server: str = "https://ntfy.sh",
        auth: tuple[str, str] | str | None = None,
    ) -> None:
        """Itinialize the NtfyClient.

        Args:
            topic: The topic to use for this client
            server: The server to connect to. Must include the protocol (http/https)
            auth: The authentication credentials to use for this client. Takes precedence over environment variables. Can be a tuple of (user, password) or a token.

        Returns:
            None

        Exceptions:
            ToDo

        Examples:
            client = NtfyClient(topic="my_topic")
        """
        self._server = os.environ.get("NTFY_SERVER") or server
        self._topic = topic
        self.__set_url(self._server, topic)
        self._auth: tuple[str, str] | None = self._resolve_auth(auth)

    def _resolve_auth(
        self, auth: tuple[str, str] | str | None
    ) -> tuple[str, str] | None:
        """Resolve the authentication credentials.

        Args:
            auth: The authentication credentials to use for this client. Takes precedence over environment variables. Can be a tuple of (user, password) or a token string.

        Returns:
            tuple[str, str] | None: The authentication credentials.
        """
        # If the user has supplied credentials, use them (including empty string)
        if auth is not None:
            if isinstance(auth, tuple):
                return auth
            if isinstance(auth, str):
                return ("", auth)

        # Otherwise, check environment variables
        user = os.environ.get("NTFY_USER")
        password = os.environ.get("NTFY_PASSWORD")
        token = os.environ.get("NTFY_TOKEN")

        if user and password:
            return (user, password)

        if token:
            return ("", token)

        # If no credentials are found, return None
        return None

    def __set_url(
        self,
        server,
        topic,
    ) -> None:
        self.url = server.strip("/") + "/" + topic

    def set_topic(
        self,
        topic: str,
    ) -> None:
        """Set a new topic for the client.

        Args:
            topic: The topic to set for this client.

        Returns:
            None
        """
        self._topic = topic
        self.__set_url(self._server, self._topic)

    def get_topic(
        self,
    ) -> str:
        """Get the current topic.

        Returns:
            str: The current topic.
        """
        return self._topic
