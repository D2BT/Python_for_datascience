from typing import Any


def callLimit(limit: int):
    """Function to limit how many times a function can be called."""
    count = 0

    def callLimiter(function):
        """Function to wrap a function with the call limit."""

        def limit_function(*args: Any, **kwds: Any):
            """Function to call function if under the limit."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} called too many times")

        return limit_function

    return callLimiter


def main():
    """Function to test callLimit on f() and g()."""
    @callLimit(3)
    def f():
        """Function to print f()."""
        print("f()")

    @callLimit(1)
    def g():
        """Function to print g()."""
        print("g()")

    for _ in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
