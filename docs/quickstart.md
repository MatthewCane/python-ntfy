# Quickstart Guide

1. Install using pip with `pip3 install python-ntfy`
2. Import and instantiate the `NtfyClient`:

```python
# Import the ntfy client
from python_ntfy import NtfyClient

# With no credentials
client = NtfyClient(topic="Your topic")

# With credentials passed to the `NtfyClient` constructor (takes precedence over environment variables)
client = NtfyClient(topic="Your topic", auth=("your_username", "your_password")) # Basic auth
client = NtfyClient(topic="Your topic", auth="your_token") # Token auth

# Or set credentials from environment variables
from os import environ
environ["NTFY_USER"] = "your_username"
environ["NTFY_PASSWORD"] = "your_password"
environ["NTFY_TOKEN"] = "your_token"
client = NtfyClient(topic="Your topic")
```

3. Send a message:

```python
# Send a message
client.send("Your message here")
```
