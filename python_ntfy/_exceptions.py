class MessageSendError(Exception):
    """Exception raised when a message fails to send."""

    def __init__(self, message: str) -> None:
        """Initialize the exception.

        Args:
            message: The message to display.
        """
        self.message = message
        super().__init__(self.message)
