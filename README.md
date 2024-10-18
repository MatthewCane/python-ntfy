# A Python Library For ntfy.sh

An easy-to-use ntfy python library. Aiming for full feature support.

## Quickstart

1. Install using pip with `pip3 install python-ntfy`
2. Configure the following environment variables:
   - `NTFY_USER`: The username for your server (if required)
   - `NTFY_PASSWORD`: The password for your server (if required)
   - `NTFY_SERVER`: The server URL (defaults to https://ntft.sh)
3. Setup your application to use the library:

 ```python
 # Import the ntfy client
from python_ntfy import NtfyClient

# Create an `NtfyClient` instance with a topic
client = NtfyClient(topic="Your topic")

# Send a message
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

This project uses:

- Poetry as it's dependency manager
- Ruff for linting and code formatting

To install dev dependencies, run `poetry install --with dev`.

### Linting and Formatting

These can be run with:

- `poetry run ruff format`
- `poetry run ruff check`

### Tests

This project is aiming for 95% code coverage. Any added features must include comprihensive tests.

You can run the tests against a local instance of `ntfy` *or* `ntfy.sh`.

#### Setup Steps

1. To test against a *local* `ntfy` instance:
  i. Create a container using `docker run -p 80:80 -it binwiederhier/ntfy serve --attachment-cache-dir=/cache --base-url=http://localhost`
  ii. Set the following key in the `.env` file: `NTFY_SERVER=http://localhost`
  iii. Add a dummy username and password to `.env` (see example.env)
2. To test against https://ntfy.sh:
  i. Add username and password for ntfy.sh to `.env` (see example.env)
3. Run the tests with `poetry run pytest --cov`

The tests will sent messages to the `python_ntfy_testing` topic so you will need to subcribe to that topic to see the test messages.