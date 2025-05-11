"""Module demonstrating Python type annotations and function signatures."""


def greet(name: str) -> str:
    """Greet a name."""
    return f'Hello, {name}!'


def greet_all(names: list[str]) -> list[str]:
    """Greet all names in the list."""
    return [greet(name) for name in names]


def greet_all_with_names(names: list[str]) -> list[str]:
    """Greet all names in the list."""
    return [greet(name) for name in names]


def not_typed(name: str) -> str:
    """Greet a name."""
    return f'Hello, {name}!'


def greeting(name: str) -> str:
    """Greet a name."""
    return 'Hello ' + name


greeting('World!')  # No error
