"""Test cases for getting cached messages from the server.

async is used here because we have to wait for the messages to be sent
before we can get them, so a sleep is required.

Additional, because we are checking the first message in the list, we
need to make sure that only the message sent for testing is in the topic
so we generate a random topic for each test.
"""

import asyncio
import json
from datetime import datetime

import pytest

from python_ntfy import NtfyClient

from .helpers import random_string


@pytest.mark.asyncio
async def test_get_topic(localhost_server_no_auth, no_auth) -> None:
    message = random_string()
    topic = random_string(5)
    ntfy = NtfyClient(topic=topic)
    ntfy.send(message=message)
    await asyncio.sleep(1)
    response = ntfy.get_cached_messages()
    print(json.dumps(response, indent=2))
    assert response[0]["topic"] == topic
    assert response[0]["message"] == message
    assert len(response) > 0


@pytest.mark.asyncio
async def test_get_topic_with_limit(localhost_server_no_auth, no_auth) -> None:
    message = random_string()
    topic = random_string(5)
    ntfy = NtfyClient(topic=topic)
    ntfy.send(message=message)
    await asyncio.sleep(1)
    response = ntfy.get_cached_messages(since="1m")
    print(json.dumps(response, indent=2))
    assert response[0]["topic"] == topic
    assert response[0]["message"] == message


@pytest.mark.asyncio
async def test_get_topic_with_scheduled(localhost_server_no_auth, no_auth) -> None:
    message = random_string()
    topic = random_string(5)
    ts = datetime.fromtimestamp(int(datetime.now().timestamp()) + 10)
    ntfy = NtfyClient(topic=topic)
    response = ntfy.send(message=message, schedule=ts)
    await asyncio.sleep(1)

    response = ntfy.get_cached_messages(scheduled=True)
    print(json.dumps(response, indent=2))
    assert response[0]["topic"] == topic
    assert response[0]["message"] == message
    assert response[0]["time"] == int(ts.timestamp())
