from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path

from ._get_functions import get_cached_messages as _get_cached_messages
from ._send_functions import (
    BroadcastAction as _BroadcastAction,
    HttpAction as _HttpAction,
    MessagePriority as _MessagePriority,
    ViewAction as _ViewAction,
    send as _send_message,
    send_file as _send_file,
)


class NtfyClient:
    """A client for interacting with the ntfy notification service."""

    # Backwards-compatible attribute exposure (discouraged for new code):
    BroadcastAction = _BroadcastAction
    HttpAction = _HttpAction
    MessagePriority = _MessagePriority
    ViewAction = _ViewAction

    def __init__(
        self,
        topic: str,
        server: str = "https://ntfy.sh",
        auth: tuple[str, str] | str | None = None,
    ) -> None:
        """Initialize the client.

        Args:
            topic: The topic to use for this client.
            server: The server base URL (must include protocol, e.g., https://).
            auth: Credentials for this client. Takes precedence over environment
                variables. May be a tuple ``(user, password)`` for Basic auth
                or a token string for Bearer auth.
        """
        self._server = os.environ.get("NTFY_SERVER") or server
        self._topic = topic
        self.__set_url(self._server, topic)
        self._auth: tuple[str, str] | None = self._resolve_auth(auth)

    def _resolve_auth(
        self, auth: tuple[str, str] | str | None
    ) -> tuple[str, str] | None:
        """Resolve authentication credentials using args or environment variables."""
        # Explicitly provided credentials take precedence (including empty string)
        if auth is not None:
            if isinstance(auth, tuple):
                return auth
            if isinstance(auth, str):
                return ("", auth)

        # Fallback to environment variables
        user = os.environ.get("NTFY_USER")
        password = os.environ.get("NTFY_PASSWORD")
        token = os.environ.get("NTFY_TOKEN")

        if user and password:
            return (user, password)
        if token:
            return ("", token)

        return None

    def __set_url(self, server: str, topic: str) -> None:
        self.url = server.strip("/") + "/" + topic

    def set_topic(self, topic: str) -> None:
        """Set a new topic for this client."""
        self._topic = topic
        self.__set_url(self._server, self._topic)

    def get_topic(self) -> str:
        """Get the current topic."""
        return self._topic

    # Public API methods delegate to internal helpers for implementation

    def send(
        self,
        message: str,
        title: str | None = None,
        priority: _MessagePriority = _MessagePriority.DEFAULT,
        tags: list[str] | None = None,
        actions: list[_ViewAction | _BroadcastAction | _HttpAction] | None = None,
        schedule: datetime | None = None,
        format_as_markdown: bool = False,
        timeout_seconds: int = 5,
        email: str | None = None,
    ) -> dict:
        """Send a text-based message to the server."""
        return _send_message(
            self,
            message=message,
            title=title,
            priority=priority,
            tags=tags,
            actions=actions,
            schedule=schedule,
            format_as_markdown=format_as_markdown,
            timeout_seconds=timeout_seconds,
            email=email,
        )

    def send_file(
        self,
        file: str | Path,
        title: str | None = None,
        priority: _MessagePriority = _MessagePriority.DEFAULT,
        tags: list[str] | None = None,
        actions: list[_ViewAction | _BroadcastAction | _HttpAction] | None = None,
        schedule: datetime | None = None,
        timeout_seconds: int = 30,
        email: str | None = None,
    ) -> dict:
        """Send a file to the server."""
        return _send_file(
            self,
            file=file,
            title=title,
            priority=priority,
            tags=tags,
            actions=actions,
            schedule=schedule,
            timeout_seconds=timeout_seconds,
            email=email,
        )

    def get_cached_messages(
        self,
        since: str = "all",
        scheduled: bool = False,
        timeout_seconds: int = 10,
    ) -> list[dict]:
        """Get cached messages from the server."""
        return _get_cached_messages(
            self,
            since=since,
            scheduled=scheduled,
            timeout_seconds=timeout_seconds,
        )
