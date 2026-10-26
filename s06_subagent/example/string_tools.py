"""Small, dependency-free string helpers.

This module currently exposes a single public function, :func:`slugify`, which
turns arbitrary human-written text into a URL-friendly "slug":

    "Crème Brûlée"  ->  "creme-brulee"
    "  Hello, World!  "  ->  "hello-world"

The transformation is deliberately predictable and lossless in spirit:

1. Non-string input (including ``None``) is rejected with ``TypeError``.
2. Unicode text is NFKD-normalized and stripped of combining marks, so accented
   letters degrade to their ASCII base letter (``é`` -> ``e``, ``ï`` -> ``i``).
3. Everything is lowercased.
4. Every run of characters outside ``[a-z0-9]`` collapses into a single ``-``.
5. Leading and trailing ``-`` are removed, so punctuation-only or blank input
   yields the empty string.

Only the standard library (``re`` and ``unicodedata``) is used.
"""

import re
import unicodedata

__all__ = ["slugify"]

#: Characters that are allowed to survive into the slug (after lowercasing).
_NON_SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Convert ``text`` into a lowercase, hyphen-separated, ASCII-only slug.

    Accented characters are folded to their base letter, punctuation and
    whitespace become single hyphens, and no length truncation is performed.

    Args:
        text: The string to slugify.

    Returns:
        The slug as a ``str``; ``""`` when the input contains no usable
        ``[a-z0-9]`` characters at all.

    Raises:
        TypeError: If ``text`` is not a ``str`` (``None`` included).

    Examples:
        >>> slugify("Hello World")
        'hello-world'
        >>> slugify("Crème Brûlée")
        'creme-brulee'
        >>> slugify("!!!???")
        ''
    """
    if not isinstance(text, str):
        raise TypeError(
            "slugify() expected a str, got " + type(text).__name__
        )

    # 2. Decompose accented characters and drop the combining marks.
    normalized = unicodedata.normalize("NFKD", text)
    folded = "".join(
        char for char in normalized if not unicodedata.combining(char)
    )

    # 3. Lowercase, then 4. collapse every non-[a-z0-9] run into one hyphen.
    lowered = folded.lower()
    hyphenated = _NON_SLUG_RE.sub("-", lowered)

    # 5. Trim the separator from both ends.
    return hyphenated.strip("-")


if __name__ == "__main__":
    samples = [
        "Hello World",
        "  Hello,   World!  ",
        "Crème Brûlée",
        "--Already--Slugged--",
        "CamelCase123",
        "naïve café",
        "100% legit",
        "!!!???",
        "   \t\n ",
        "",
    ]
    print("slugify() samples")
    print("-" * 40)
    for sample in samples:
        print(f"{sample!r:<28} -> {slugify(sample)!r}")
