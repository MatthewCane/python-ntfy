import os, random, string


def clear_env():
    os.environ.pop("NTFY_USER", None)
    os.environ.pop("NTFY_PASSWORD", None)


def get_topic():
    return "python_ntfy_testing"


def random_string(length=10):
    return "".join([random.choice(string.ascii_lowercase) for _ in range(length)])
