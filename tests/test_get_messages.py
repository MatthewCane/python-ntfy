"""Test cases for getting cached messages from the server.

async is used here because we have to wait for the messages to be sent
before we can get them, so a sleep is required.
"""

import asyncio
import json

import pytest

from python_ntfy import NtfyClient

from .helpers import random_string, topic


@pytest.mark.asyncio
async def test_get_topic(localhost_server, no_auth) -> None:
    message = random_string()
    ntfy = NtfyClient(topic=topic)
    ntfy.send(message=message)
    await asyncio.sleep(1)
    response = ntfy.get_cached_messages()
    print(json.dumps(response, indent=2))
    assert response[0]["topic"] == topic
    assert response[0]["message"] == message
    assert len(response) > 0


@pytest.mark.asyncio
async def test_get_topic_with_limit(localhost_server, no_auth) -> None:
    message = random_string()
    ntfy = NtfyClient(topic=topic)
    ntfy.send(message=message)
    await asyncio.sleep(1)
    response = ntfy.get_cached_messages(since="1m")
    print(json.dumps(response, indent=2))
    assert response[0]["topic"] == topic
    assert response[0]["message"] == message
