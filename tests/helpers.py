import random
import string

topic = "python_ntfy_testing"


def random_string(length: int = 32) -> str:
    return "".join([random.choice(string.ascii_lowercase) for _ in range(length)])  # noqa: S311
