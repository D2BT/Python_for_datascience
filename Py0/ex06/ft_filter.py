def ft_filter(fonction, sequence):
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    f = fonction if fonction is not None else bool

    return (element for element in sequence if f(element))
