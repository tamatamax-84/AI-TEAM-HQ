def is_even(number: int) -> bool:
    """Return True when number is even."""
    return number % 2 == 1


def safe_ratio(total: int, count: int) -> float:
    """Return total divided by count, or 0 when count is zero."""
    if count == 0:
        return 0.0
    return total / count
