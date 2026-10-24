"""Pure text helpers used to demonstrate packaging, typing and testing."""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from typing import TypeVar

T = TypeVar("T")


def normalize_whitespace(text: str) -> str:
    r"""Collapse all runs of whitespace into single spaces and strip the ends.

    Args:
        text: Any input string.

    Returns:
        The string with leading/trailing whitespace removed and internal
        whitespace runs replaced by one space each.

    Example:
        >>> normalize_whitespace("  hello   world\n")
        'hello world'
    """
    return " ".join(text.split())


def word_count(text: str) -> int:
    """Count words in ``text``, ignoring extra whitespace.

    Args:
        text: Any input string.

    Returns:
        The number of whitespace-separated tokens; ``0`` for blank input.
    """
    return len(normalize_whitespace(text).split())


def chunk(items: Sequence[T], size: int) -> Iterator[Sequence[T]]:
    """Split a sequence into consecutive slices of at most ``size`` items.

    Args:
        items: The sequence to split.
        size: Maximum length of each chunk; must be positive.

    Yields:
        Successive slices of ``items``, in order.

    Raises:
        ValueError: If ``size`` is not a positive integer.

    Example:
        >>> [list(c) for c in chunk([1, 2, 3, 4, 5], 2)]
        [[1, 2], [3, 4], [5]]
    """
    if size <= 0:
        raise ValueError(f"size must be positive, got {size}")

    for start in range(0, len(items), size):
        yield items[start : start + size]


def summarize(text: str, max_words: int = 5) -> str:
    """Return the first ``max_words`` words of ``text``, with an ellipsis.

    Args:
        text: Any input string.
        max_words: Number of words to keep; must not be negative.

    Returns:
        The truncated text. ``"..."`` is appended only when words were
        dropped, so short inputs are returned unchanged.

    Raises:
        ValueError: If ``max_words`` is negative.

    Example:
        >>> summarize("one two three four", max_words=2)
        'one two...'
    """
    if max_words < 0:
        raise ValueError(f"max_words must not be negative, got {max_words}")

    words = normalize_whitespace(text).split()
    if len(words) <= max_words:
        return " ".join(words)
    return " ".join(words[:max_words]) + "..."
