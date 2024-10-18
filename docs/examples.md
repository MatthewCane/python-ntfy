# Example Usage

## Send a basic message

```python
client = NtfyClient(topic="Your topic")

client.send("Your message here")
```

## Send a markdown formatted message

```python
client = NtfyClient(topic="Your topic")

message = """# My Message

- Bullet
- Points
"""

client.send(message, format_as_markdown=True)
```

## Send a message with an attachment

```python
client = NtfyClient(topic="Your topic")

client.send("Your message here", attachment="/path/to/your/file.txt")
```

## Send a message with priority

```python
client = NtfyClient(topic="Your topic")

client.send("Your message here", priority=client.MessagePriority.HIGH)
```

## Send a message with tags

```python
client = NtfyClient(topic="Your topic")

client.send("Your message here", tags=["tag1", "tag2"])
```

## Send a message with click action

```python
client = NtfyClient(topic="Your topic")

client.send("Your message here", actions=[client.ViewAction(label="Open Website", url="https://ntfy.sh"),])
```
