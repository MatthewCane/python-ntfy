"""Compatibility shim for historical import path.

Prefer importing from `python_ntfy` package root:

    from python_ntfy import NtfyClient

This module re-exports `NtfyClient` to maintain backward compatibility with
older references like `python_ntfy._ntfy.NtfyClient`.
"""

from warnings import warn

from .client import NtfyClient as NtfyClient

warn(
    "`python_ntfy._ntfy` is deprecated and will be removed in a future version. Please import from `python_ntfy` instead.",
    DeprecationWarning,
    stacklevel=2,
)
