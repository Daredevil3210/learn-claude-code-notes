"""Minimal greeting example used by the s05_todo_write lesson."""


def greet(name: str) -> str:
    """Build a greeting message for ``name``.

    Args:
        name: Name of the person to greet.

    Returns:
        The greeting text, e.g. ``"Hello, Claude"``.
    """
    return f"Hello, {name}"


def main() -> None:
    """Run the example: greet a hard-coded name and print the result."""
    print(greet("Claude"))


if __name__ == "__main__":
    main()
