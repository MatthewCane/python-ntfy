class NtfyMessageError(Exception):
    """Base exception for ntfy message errors."""

    def __init__(self, message: str) -> None:
        """Initialize the exception.

        Args:
            message: The message to display.
        """
        self.message = message
        super().__init__(self.message)


class MessageSendError(NtfyMessageError):
    """Exception raised when a message fails to send."""


class MessageReceiveError(NtfyMessageError):
    """Exception raised when a message fails to retrieved."""
