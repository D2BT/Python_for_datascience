def slice_me(family: list, start: int, end: int) -> list:
    """
    Print the shape of family (rows, cols), then return a
    truncated copy of family sliced between start and end
    (using list slicing, not a manual loop). Handle invalid
    input: family not a list, rows of different lengths, etc.
    """
    try:
        if not isinstance(family, list):
            raise TypeError("family must be a list")
        if not isinstance(start, (int)):
            raise TypeError("start must be an int")
        if not isinstance(end, (int)):
            raise TypeError("end must be an int")
        if len(family) == 0:
            raise ValueError("family must not be empty")
        row_length = len(family[0])
        for row in family:
            if not isinstance(row, list):
                raise TypeError("family must be a list of lists")
            if len(row) != row_length:
                raise ValueError("all rows in family must"
                                 " have the same length")
        print(f"My shape is : ({len(family)}, {row_length})")
        print(f"My new shape is : ({len(family[start:end])}, {row_length})")
        return family[start:end]
    except (TypeError, ValueError) as e:
        print(f"slice_me: error: {e}")
        return None


def main():
    """
    Test slice_me with the subject's example family and check
    the printed shapes / returned slices match the expected
    output, plus a couple of invalid inputs.
    """
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

    # error cases you're expected to handle without crashing
    print(slice_me("not a list", 0, 2))
    print(slice_me([[1, 2], [3]], 0, 2))


if __name__ == "__main__":
    main()
