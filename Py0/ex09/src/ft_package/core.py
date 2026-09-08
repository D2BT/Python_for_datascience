"""Core functions of ft_package."""


def count_in_list(lst: list, item) -> int:
    """Return the number of occurrences of item in lst."""
    if not isinstance(lst, list):
        raise TypeError("lst must be a list")
    return lst.count(item)
