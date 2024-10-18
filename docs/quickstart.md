# Quickstart Guide

1. Install using pip with `pip3 install python-ntfy`
2. Configure the following environment variables:
    - `NTFY_USER`: The username for your server (if required)
    - `NTFY_PASSWORD`: The password for your server (if required)
    - `NTFY_SERVER`: The server URL (defaults to `https://ntft.sh`)
3. Setup your application to use the library:

```python
# Import the ntfy client
from python_ntfy import NtfyClient

# Create an `NtfyClient` instance with a topic
client = NtfyClient(topic="Your topic")

# Send a message
client.send("Your message here")
```
