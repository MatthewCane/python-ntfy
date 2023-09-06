from python_ntfy import NtfyClient
import pytest, dotenv, json, asyncio
from .helpers import *


@pytest.mark.asyncio
async def test_get_topic():
    topic = get_topic()
    message = random_string()
    dotenv.load_dotenv()
    ntfy = NtfyClient(topic=topic)
    ntfy.send(message=message)
    await asyncio.sleep(1)
    response = ntfy.get_cached_messages()
    print(json.dumps(response, indent=2))
    assert response[0]["topic"] == topic
    assert response[0]["message"] == message
    assert len(response) > 0


@pytest.mark.asyncio
async def test_get_topic_with_limit():
    topic = get_topic()
    message = random_string()
    dotenv.load_dotenv()
    ntfy = NtfyClient(topic=topic)
    ntfy.send(message=message)
    await asyncio.sleep(1)
    response = ntfy.get_cached_messages(since="1m")
    print(json.dumps(response, indent=2))
    assert response[0]["topic"] == topic
    assert response[0]["message"] == message
