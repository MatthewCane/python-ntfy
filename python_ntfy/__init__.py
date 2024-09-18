import os

class NtfyClient:
    from ._send_functions import send, send_file, MessagePriority
    from ._get_functions import get_cached_messages

    def __init__(
        self,
        topic: str,
        server: str = "https://ntfy.sh",
    ):
        """
        :param topic: The topic to use for this client
        :param server: The server to connect to. Must include the protocol (http/https)
        :return:
        """
        self._server = os.environ.get("NTFY_SERVER") or server
        self._topic = topic
        self.__set_url(server, topic)

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
