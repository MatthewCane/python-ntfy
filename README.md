# A Python Library For ntfy

![GitHub Release](https://img.shields.io/github/v/release/MatthewCane/python-ntfy?display_name=release&label=latest%20release&link=https%3A%2F%2Fgithub.com%2FMatthewCane%2Fpython-ntfy%2Freleases%2Flatest)
![PyPI - Downloads](https://img.shields.io/pypi/dm/python-ntfy?logo=pypi&link=http%3A%2F%2Fpypi.org%2Fproject%2Fpython-ntfy%2F)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/MatthewCane/python-ntfy/publish.yml?logo=githubactions&link=https%3A%2F%2Fgithub.com%2FMatthewCane%2Fpython-ntfy%2Factions%2Fworkflows%2Fpublish.yml)

An easy-to-use python library for the [ntfy notification service](https://ntfy.sh/). Aiming for full feature support and a super easy to use interface.

## Quickstart

1. Install using pip with `pip3 install python-ntfy`
2. Use the `NtfyClient` to send messages:

```python
# Import the ntfy client
from python_ntfy import NtfyClient

# Create an `NtfyClient` instance with a topic
client = NtfyClient(topic="Your topic")

# Send a message
client.send("Your message here")
```

For information on setting up authentication, see the [quickstart guide](https://matthewcane.github.io/python-ntfy/quickstart/).

## Documentation

See the full documentation at [https://matthewcane.github.io/python-ntfy/](https://matthewcane.github.io/python-ntfy/).

## Supported Features

- Username + password auth
- Access token auth
- Custom servers
- Sending plaintext messages
- Sending Markdown formatted text messages
- Scheduling messages
- Retrieving cached messages
- Scheduled delivery
- Tags
- Action buttons
- Email notifications

## Contributing

We welcome contributions! This project aims to provide a complete and user-friendly Python library for ntfy. Here's how you can help:

### Prerequisites

Before contributing, you'll need to install these tools:

- **[uv](https://github.com/astral-sh/uv)** - Fast Python package manager and installer
- **[Just](https://github.com/casey/just)** - Command runner for project tasks
- **[Docker](https://www.docker.com/)** and **[Docker Compose](https://docs.docker.com/compose/)** - For running tests with ntfy servers
- **[Pre-commit](https://pre-commit.com/)** - Git hooks for code quality (optional but recommended)

### Development Steps

- Fork the repository and make your changes
- Run `just setup` to install the pre-commit hooks
- Run `just format` to format the code
- Run `just test` to run all the tests
- Create a pull request with detailed description of your changes

Thank you for contributing to python-ntfy! 🚀
