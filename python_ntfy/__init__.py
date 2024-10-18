import os


class NtfyClient:
    # The functions need to be imported here to:
    # 1. Keep the functions in a separate file
    # 2. Keep the docstrings working in the IDE
    # 3. Allow the functions to be called with self
    # MyPy does not like this, but it works
    from ._send_functions import (  # type: ignore
        send,
        send_file,
        MessagePriority,
        ViewAction,
        BroadcastAction,
        HttpAction,
    )
    from ._get_functions import get_cached_messages  # type: ignore

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
