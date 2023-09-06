# ntfy.sh Python Library

An easy-to-use ntfy python library. Aiming for full feature support.

## Quickstart

1. Install using pip with `pip3 install python-ntfy`
2. If you are using a server that requires auth, set the env vars
3. Import the library

 ```python
from python_ntfy import NtfyClient
 ```

4. Create an `NtfyClient` instance with a topic

```python
client = NtfyClient(topic="Your topic")
```

5. Send a message

```python
client.send("Your message here")
```

## Supported Features

- Username + password auth
- Custom servers
- Sending plaintext messages
- Sending Markdown formatted text messages
- Retrieving cached messages
- Scheduled delivery

## Future Features

- Access token auth
- Email notifications
- Tags
- Action buttons
- Send to multiple topics at once

## Test and Development

This project uses Poetry. 

### Tests

This project is aiming for 95% code coverage. Any added features must include comprihensive tests.

To run tests:

1. `poetry install --include test`
2. Add username and password for ntfy.sh to `.env`
3. `poetry run pytest --cov`
