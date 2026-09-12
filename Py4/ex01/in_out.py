def square(x: int | float) -> int | float:
    """Function to return the square of x."""
    return (x ** 2)


def pow(x: int | float) -> int | float:
    """Function to return x to the power of itself."""
    return (x ** x)


def outer(x: int | float, function) -> object:
    """Function to create a counter that reapplies function."""
    count = 0

    def inner() -> float:
        """Function to apply function one more time than before."""
        nonlocal count
        count += 1
        result = x
        for _ in range(count):
            result = function(result)
        return result

    return inner


def main():
    """Function to test outer with square and pow."""
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
