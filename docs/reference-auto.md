# NtfyClient Documentation

## Overview

NtfyClient is a Python package for interacting with the ntfy.sh service or a self-hosted ntfy server. It provides functionality to send notifications and retrieve cached messages.

## Installation

You can install NtfyClient using pip:

```bash
pip install ntfyclient
```

## Usage

### Initializing the Client

```python
from ntfyclient import NtfyClient

client = NtfyClient(topic="your_topic", server="https://ntfy.sh")
```

## API Reference

### NtfyClient

#### `__init__(topic: str, server: str = "https://ntfy.sh")`

Initialize a new NtfyClient instance.

- `topic`: The topic to use for this client
- `server`: The server to connect to. Must include the protocol (http/https)

#### `set_topic(topic: str)`

Set a new topic for the client.

- `topic`: The new topic to use for this client

### Sending Messages

#### `send(message: str, title: str = None, priority: Optional[MessagePriority] = MessagePriority.DEFAULT, tags: list = [], actions: list[Union[ViewAction, BroadcastAction, HttpAction, None]] = [], format_as_markdown: bool = False)`

Send a text-based message to the server.

- `message`: The message to send
- `title`: The title of the message (optional)
- `priority`: The priority of the message (optional, defaults to `MessagePriority.DEFAULT`)
- `tags`: A list of tags to attach to the message (optional)
- `actions`: A list of Action objects to attach to the message (optional)
- `format_as_markdown`: If true, the message will be formatted as markdown (optional)

Returns the response from the server.

#### `send_file(file: str, title: str = None, priority: Optional[MessagePriority] = MessagePriority.DEFAULT, tags: list = [], actions: list[Union[ViewAction, BroadcastAction, HttpAction, None]] = [])`

Send a file to the server.

- `file`: The path to the file to send
- `title`: The title of the file (optional)
- `priority`: The priority of the message (optional, defaults to `MessagePriority.DEFAULT`)
- `tags`: A list of tags to attach to the message (optional)
- `actions`: A list of Action objects to attach to the message (optional)

Returns the response from the server.

### Retrieving Messages

#### `get_cached_messages(since: str = "all", scheduled: bool = False)`

Get cached messages from the server.

- `since`: The timestamp to start from. If set to "all", will return all messages (optional)
- `scheduled`: If true, will return scheduled messages (optional)

Returns a list of messages.

### Enums and Classes

#### MessagePriority

An enumeration of message priority levels:

- `MIN`: "1"
- `LOW`: "2"
- `DEFAULT`: "3"
- `HIGH`: "4"
- `MAX`: "5"
- `URGENT`: Alias for MAX

#### ActionType

An enumeration of action button types:

- `VIEW`: "view"
- `BROADCAST`: "broadcast"
- `HTTP`: "http"

#### ViewAction

Represents a view action button.

- `__init__(label: str, url: str, clear: bool = False)`

#### BroadcastAction

Represents a broadcast action button.

- `__init__(label: str, intent: str = "io.heckel.ntfy.USER_ACTION", extras: Optional[dict] = None, clear: bool = False)`

#### HttpAction

Represents an HTTP action button.

- `__init__(label: str, url: str, method: str = "POST", headers: Optional[dict] = None, body: Optional[str] = None, clear: bool = False)`

## Examples

### Sending a Simple Message

```python
from ntfyclient import NtfyClient, MessagePriority

client = NtfyClient("your_topic")
response = client.send(
    message="Hello, world!",
    title="Test Message",
    priority=MessagePriority.HIGH,
    tags=["test", "example"]
)
print(response)
```

### Sending a File

```python
from ntfyclient import NtfyClient

client = NtfyClient("your_topic")
response = client.send_file("path/to/your/file.txt", title="Important File")
print(response)
```

### Retrieving Cached Messages

```python
from ntfyclient import NtfyClient

client = NtfyClient("your_topic")
messages = client.get_cached_messages(since="2023-01-01")
for message in messages:
    print(f"Message: {message['message']}, Time: {message['time']}")
```

### Using Action Buttons

```python
from ntfyclient import NtfyClient, ViewAction, BroadcastAction, HttpAction

client = NtfyClient("your_topic")
actions = [
    ViewAction("Open Website", "https://example.com"),
    BroadcastAction("Custom Action", extras={"key": "value"}),
    HttpAction("API Call", "https://api.example.com", method="POST", body='{"key": "value"}')
]
response = client.send(
    message="Message with actions",
    title="Action Test",
    actions=actions
)
print(response)
```

## Environment Variables

The NtfyClient supports the following environment variables:

- `NTFY_SERVER`: Sets the default server URL
- `NTFY_USER`: Sets the username for authentication
- `NTFY_PASSWORD`: Sets the password for authentication

If both `NTFY_USER` and `NTFY_PASSWORD` are set, the client will use them for authentication.