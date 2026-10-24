"""Small demo package for the s05_todo_write lesson.

This package exposes a handful of pure utility helpers that are easy to
type-hint, document and unit-test.

Example:
    >>> from demo_pkg import word_count
    >>> word_count("hello demo world")
    3
"""

from .utils import chunk, normalize_whitespace, summarize, word_count

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "chunk",
    "normalize_whitespace",
    "summarize",
    "word_count",
]
