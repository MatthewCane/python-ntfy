# Reference Guide

## `NtfyClient`

## Initialiser

```python
from python_ntfy import NtfyClient

NtfyClient(
  topic: str,
  server: str = "https://ntfy.sh"
)
```

### Arguments

**`topic` (required)**

Type: String
The topic to send messages to.

**`server`**

Type: String  
Default: `https://ntfy.sh`  
The server to send messages to.

---

### Methods

#### `send`

```python
NtfyClient.send(
  message: str,
  title: str = None,
  priority: Optional[MessagePriority] = MessagePriority.DEFAULT,
  tags: list = [],
  actions: list[Union[ViewAction, BroadcastAction, HttpAction, None]] = [],
  format_as_markdown: bool = False,
) -> dict
```

##### Arguments

**`message` (required)**

Type: String  
The message to send to the topic.

**`title`**

Type: String  
Default: `None`  
The title of the message. If `None`, the message will have no title.

**`priority`**

Type: `Optional[MessagePriority]`  
Default: `MessagePriority.DEFAULT`  
The priority of the message. Can be one of the values from the `MessagePriority` enum.

**`tags`**

Type: `list`  
Default: `[]`  
A list of tags to associate with the message.

**`actions`**

Type: `list[Union[ViewAction, BroadcastAction, HttpAction, None]]`  
Default: `[]`  
A list of actions to include with the message. Each action can be an instance of `ViewAction`, `BroadcastAction`, `HttpAction`, or `None`.

**`format_as_markdown`**

Type: `bool`  
Default: `False`  
If `True`, the message will be formatted as Markdown.

#### `send_file`

```python
NtfyClient.send_file(
    file: str,
    title: str = None,
    priority: Optional[MessagePriority] = MessagePriority.DEFAULT,
    tags: list = [],
    actions: list[Union[ViewAction, BroadcastAction, HttpAction, None]] = [],
) -> dict
```

#### `set_topic`

```python
NtfyClient.set_topic(topic: str) -> None
```

##### Arguments

**`topic` (required)**  
Type: `str`  
The topic to send messages to.

#### `get_cached_messages`

```python
NtfyClient.get_cached_messages(
    since: str = "all",
    scheduled: bool = False
)
```

##### Arguments

**`since`**

Type: `str`  
Default: `"all"`  
The timestamp to start retrieving messages from. If set to "all", will return all messages.

**`scheduled`**

Type: `bool`  
Default: `False`  
If `True`, will return scheduled messages.

##### Returns

Type: `list`  
A list of dictionaries containing the cached messages.

---

### Classes

#### `ViewAction`

```python
ViewAction(
    label: str,
    url: str,
    clear: bool = False
)
```

##### Arguments

**`label` (required)**

Type: `str`  
The label for the view action button.

**`url` (required)**

Type: `str`  
The URL to open when the action button is clicked.

**`clear`**

Type: `bool`  
Default: `False`  
If `True`, the notification will be cleared when the action is tapped.

#### `BroadcastAction`

```python
BroadcastAction(
    label: str,
    intent: str = "io.heckel.ntfy.USER_ACTION",
    extras: Optional[dict] = None,
    clear: bool = False
)
```

##### Arguments

**`label` (required)**

Type: `str`  
The label for the broadcast action button.

**`intent`**

Type: `str`  
Default: `"io.heckel.ntfy.USER_ACTION"`  
The Android intent to broadcast when the action is tapped.

**`extras`**

Type: `Optional[dict]`  
Default: `None`  
Additional key-value pairs to add to the broadcast intent.

**`clear`**

Type: `bool`  
Default: `False`  
If `True`, the notification will be cleared when the action is tapped.

#### `HttpAction`

```python
HttpAction(
    label: str,
    url: str,
    method: str = "POST",
    headers: Optional[dict] = None,
    body: Optional[str] = None,
    clear: bool = False
)
```

##### Arguments

**`label` (required)**

Type: `str`  
The label for the HTTP action button.

**`url` (required)**

Type: `str`  
The URL to send the HTTP request to when the action is tapped.

**`method`**

Type: `str`  
Default: `"POST"`  
The HTTP method to use for the request.

**`headers`**

Type: `Optional[dict]`  
Default: `None`  
Additional headers to include in the HTTP request.

**`body`**

Type: `Optional[str]`  
Default: `None`  
The body of the HTTP request.

**`clear`**

Type: `bool`  
Default: `False`  
If `True`, the notification will be cleared when the action is tapped.

---

### Enums

#### `MessagePriority`

An enumeration of message priority levels.

```python
class MessagePriority(Enum):
    MIN = "1"
    LOW = "2"
    DEFAULT = "3"
    HIGH = "4"
    MAX = "5"
    URGENT = MAX
```

#### `ActionType`

An enumeration of action button types.

```python
class ActionType(Enum):
    VIEW = "view"
    BROADCAST = "broadcast"
    HTTP = "http"
```
