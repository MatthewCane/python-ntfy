# A Python Library For ntfy

![PyPI - Version](https://img.shields.io/pypi/v/python-ntfy?link=https%3A%2F%2Fpypi.org%2Fproject%2Fpython-ntfy%2F)
![PyPI - Downloads](https://img.shields.io/pypi/dm/python-ntfy?link=https%3A%2F%2Fpypistats.org%2Fpackages%2Fpython-ntfy)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/MatthewCane/python-ntfy/publish.yml?link=https%3A%2F%2Fgithub.com%2FMatthewCane%2Fpython-ntfy%2Factions%2Fworkflows%2Fpublish.yml)

An easy-to-use python library for the [ntfy notification service](https://ntfy.sh/). Aiming for full feature support and a super easy to use interface.

## Quickstart

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

See the full documentation site at [https://matthewcane.github.io/python-ntfy/](https://matthewcane.github.io/python-ntfy/).

## Supported Features

- Username + password auth
- Access token auth
- Custom servers
- Sending plaintext messages
- Sending Markdown formatted text messages
- Retrieving cached messages
- Scheduled delivery
- Tags
- Action buttons

## Future Features

- [Email notifications](https://docs.ntfy.sh/publish/#e-mail-notifications)
- Send to multiple topics at once

## Testing and Development

This project uses:

- [Poetry](https://python-poetry.org/) as it's dependency manager
- [Ruff](https://docs.astral.sh/ruff/) for linting and code formatting
- [MyPy](https://mypy-lang.org/) for static type checking
- [Pre-Commit](https://pre-commit.com/) for running the above tools before committing

To install dev dependencies, run `poetry install --with dev`.

To install pre-commit hooks, run `pre-commit install`.

### Linting, Formatting and Type Checking

These can be run with:

- `poetry run ruff format`
- `poetry run ruff check`
- `poetry run mypy .`

These tools are also run in the CI pipeline and must pass before merging.

### Tests

This project is aiming for 95% code coverage. Any added features must include comprihensive tests.

You can run the tests against a local instance of `ntfy` *or* `ntfy.sh`.

#### Setup Steps

1. To test against a *local* `ntfy` instance:
    i. Create a container using `docker run -p 80:80 -it binwiederhier/ntfy serve --attachment-cache-dir=/cache --base-url=http://localhost`
    ii. Set the following key in the `.env` file: `NTFY_SERVER=http://localhost`
    iii. Add a dummy username and password to `.env` (see example.env)
2. To test against `https://ntfy.sh`:
    i. Add username and password for ntfy.sh to `.env` (see example.env)
3. Run the tests with `poetry run pytest --cov`

The tests will sent messages to the `python_ntfy_testing` topic so you will need to subcribe to that topic to see the test messages.
