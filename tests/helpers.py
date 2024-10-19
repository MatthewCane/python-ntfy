import os
import random
import string


def clear_env(server: bool = True, user: bool = True) -> None:
    if user:
        os.environ.pop("NTFY_USER", None)
        os.environ.pop("NTFY_PASSWORD", None)
    if server:
        os.environ.pop("NTFY_SERVER", None)


def get_topic() -> str:
    return "python_ntfy_testing"


def random_string(length: int = 10) -> str:
    return "".join([random.choice(string.ascii_lowercase) for _ in range(length)])  # noqa: S311
