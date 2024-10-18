import os
from types import MethodType
from ._send_functions import (
    send,
    send_file,
    MessagePriority,
    ViewAction,
    BroadcastAction,
    HttpAction,
)
from ._get_functions import get_cached_messages


class NtfyClient:
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
        # Bind the imported functions to the class
        self.send = MethodType(send, self)
        self.send_file = MethodType(send_file, self)
        self.MessagePriority = MethodType(MessagePriority, self)
        self.get_cached_messages = MethodType(get_cached_messages, self)

        # These are Enums that don't need to be bound
        self.ViewAction = ViewAction
        self.BroadcastAction = BroadcastAction
        self.HttpAction = HttpAction

        self._server = os.environ.get("NTFY_SERVER") or server
        self._topic = topic
        self.__set_url(self._server, topic)

        if (user := os.environ.get("NTFY_USER")) and (
            password := os.environ.get("NTFY_PASSWORD")
        ):
            self._auth = (user, password)
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
