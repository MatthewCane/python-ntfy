import json

import requests

from python_ntfy._exceptions import MessageReceiveError


def get_cached_messages(
    self,
    since: str = "all",
    scheduled: bool = False,
    timeout_seconds: int = 10,
) -> list[dict]:
    """Get cached messages from the server.

    Args:
        since: The timestamp to start from. If set to "all", will return all messages.
        scheduled: If true, will return scheduled messages.
        timeout_seconds: The number of seconds to wait for the response.

    Returns:
        A list of messages.

    Raises:
        MessageReceiveError: If the request fails or the response is invalid.

    Examples:
        >>> response = client.get(since="all")

        >>> response = client.get(since="all", scheduled=True)

        >>> response = client.get(since="2019-01-01")

        >>> response = client.get(since="2019-01-01", scheduled=True)
    """
    params = {"poll": "1"}
    if scheduled:
        params.update({"scheduled": str(scheduled)})
    if since:
        params.update({"since": since})

    try:
        response = requests.get(
            url=self.url + "/json",
            params=params,
            auth=self._auth,
            timeout=timeout_seconds,
        )
        response.raise_for_status()
        messages = [json.loads(line) for line in response.text.strip().splitlines()]
    except requests.exceptions.RequestException as e:
        error_message = f"Failed to receive messages: {e}"
        raise MessageReceiveError(error_message) from e

    # Reverse the list so that the most recent notification is first
    return sorted(messages, key=lambda x: x["time"], reverse=True)
