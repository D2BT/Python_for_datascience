def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    test = function if function is not None else bool
    for element in iterable:
        if test(element):
            yield element


def main():
    """Test ft_filter against the subject's example."""
    print(list(ft_filter(lambda x: x % 2 == 0, range(10))))


if __name__ == "__main__":
    main()
