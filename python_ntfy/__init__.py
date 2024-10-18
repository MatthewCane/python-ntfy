"""This module provides the NtfyClient class for interacting with the ntfy notification service.

The NtfyClient class allows users to send notifications, files, and perform various actions
through the ntfy.sh service. It also supports retrieving cached messages.

Typical usage example:

    client = NtfyClient(topic="my_topic")
    client.send("Hello, World!")
"""

import os


class NtfyClient:
    # The functions need to be imported here to:
    # 1. Keep the functions in a separate file
    # 2. Keep the docstrings working in the IDE
    # 3. Allow the functions to be called with self
    # MyPy does not like this, but it works
    from ._get_functions import get_cached_messages  # type: ignore
    from ._send_functions import (  # type: ignore
        BroadcastAction,
        HttpAction,
        MessagePriority,
        ViewAction,
        send,
        send_file,
    )

    def __init__(
        self,
        topic: str,
        server: str = "https://ntfy.sh",
    ) -> None:
        """
        :param topic: The topic to use for this client
        :param server: The server to connect to. Must include the protocol (http/https)
        :return None:
        """

        self._server = os.environ.get("NTFY_SERVER") or server
        self._topic = topic
        self.__set_url(self._server, topic)

        # If the user has set the user and password, use that
        # If the user has set the token, use that
        # Otherwise, use an empty user and token
        if (user := os.environ.get("NTFY_USER")) and (
            password := os.environ.get("NTFY_PASSWORD")
        ):
            self._auth = (user, password)
        elif token := os.environ.get("NTFY_TOKEN"):
            self._auth = ("", token)
        else:
            self._auth = ("", "")

    def __set_url(self, server, topic):
        self.url = server.strip("/") + "/" + topic

    def set_topic(self, topic: str):
        """
        Set a new topic for the client

        :param topic: The topic to use for this client
        :return: None
        """
        self._topic = topic
        self.__set_url(self._server, self._topic)

    def get_topic(self):
        """
        Get the current topic

        :return: str
        """
        return self._topic
