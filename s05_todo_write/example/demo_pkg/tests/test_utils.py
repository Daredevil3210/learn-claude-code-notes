"""Tests for :mod:`demo_pkg.utils`.

Run from ``s05_todo_write/example`` so that ``demo_pkg`` is importable::

    python -m pytest demo_pkg -q
"""

from __future__ import annotations

import pytest

from demo_pkg import chunk, normalize_whitespace, summarize, word_count
from demo_pkg.utils import chunk as chunk_from_module


class TestNormalizeWhitespace:
    """Coverage for :func:`demo_pkg.utils.normalize_whitespace`."""

    @pytest.mark.parametrize(
        ("raw", "expected"),
        [
            ("  hello   world\n", "hello world"),
            ("single", "single"),
            ("", ""),
            ("   \t\n ", ""),
            ("a\tb\r\nc", "a b c"),
            ("already clean", "already clean"),
        ],
    )
    def test_collapses_and_strips(self, raw: str, expected: str) -> None:
        assert normalize_whitespace(raw) == expected


class TestWordCount:
    """Coverage for :func:`demo_pkg.utils.word_count`."""

    @pytest.mark.parametrize(
        ("text", "expected"),
        [
            ("hello demo world", 3),
            ("  padded   text  ", 2),
            ("", 0),
            ("   ", 0),
            ("one", 1),
        ],
    )
    def test_counts_tokens(self, text: str, expected: int) -> None:
        assert word_count(text) == expected


class TestChunk:
    """Coverage for :func:`demo_pkg.utils.chunk`."""

    def test_splits_evenly(self) -> None:
        assert [list(part) for part in chunk([1, 2, 3, 4], 2)] == [
            [1, 2],
            [3, 4],
        ]

    def test_last_chunk_may_be_shorter(self) -> None:
        assert [list(part) for part in chunk("abcde", 2)] == [
            ["a", "b"],
            ["c", "d"],
            ["e"],
        ]

    def test_size_larger_than_input(self) -> None:
        assert [list(part) for part in chunk([1, 2, 3], 10)] == [[1, 2, 3]]

    def test_empty_input_yields_nothing(self) -> None:
        assert list(chunk([], 3)) == []

    @pytest.mark.parametrize("bad_size", [0, -1, -100])
    def test_rejects_non_positive_size(self, bad_size: int) -> None:
        with pytest.raises(ValueError, match="size must be positive"):
            list(chunk([1, 2, 3], bad_size))

    def test_is_lazy(self) -> None:
        """The generator should not consume anything until iterated."""
        assert hasattr(chunk([1, 2, 3], 2), "__next__")

    def test_reexported_from_package_init(self) -> None:
        assert chunk is chunk_from_module


class TestSummarize:
    """Coverage for :func:`demo_pkg.utils.summarize`."""

    def test_truncates_long_text(self) -> None:
        assert summarize("one two three four", max_words=2) == "one two..."

    def test_keeps_short_text_unchanged(self) -> None:
        assert summarize("just a few words") == "just a few words"

    def test_exact_length_is_not_truncated(self) -> None:
        assert summarize("one two three", max_words=3) == "one two three"

    def test_normalizes_whitespace_first(self) -> None:
        assert summarize("  one\n\ttwo   three  ", max_words=2) == "one two..."

    def test_zero_words(self) -> None:
        assert summarize("anything here", max_words=0) == "..."

    def test_rejects_negative_max_words(self) -> None:
        with pytest.raises(ValueError, match="must not be negative"):
            summarize("some text", max_words=-1)
