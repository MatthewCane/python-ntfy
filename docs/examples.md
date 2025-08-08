# Example Usage

## Set up the client with no credentials

```python
client = NtfyClient(topic="Your topic")
```


## Set up the client with username and password credentials passed to the `NtfyClient` constructor

```python
client = NtfyClient(topic="Your topic", auth=("your_username", "your_password"))
```

## Set up the client with a bearer token passed to the `NtfyClient` constructor

```python
client = NtfyClient(topic="Your topic", auth="your_token")
```

## Set up the client with username and password credentials from environment variables

```python
environ["NTFY_USER"] = "your_username"
environ["NTFY_PASSWORD"] = "your_password"
client = NtfyClient(topic="Your topic")
```

## Set up the client with a bearer token from environment variables

```python
environ["NTFY_TOKEN"] = "your_token"
client = NtfyClient(topic="Your topic")
```

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

## Send a file as an attachment

```python
client = NtfyClient(topic="Your topic")

client.send_file("/path/to/your/file.txt")
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
