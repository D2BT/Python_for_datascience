class calculator:
    """A calculator for in-place scalar operations on a vector."""

    def __init__(self, vector: list[float]):
        """Function to initialize the calculator with a vector of floats"""
        self.vector = vector

    def __add__(self, scalar: float) -> None:
        """Function to add a scalar to the calculator's vector"""
        self.vector = [value + scalar for value in self.vector]
        print(self.vector)

    def __mul__(self, scalar: float) -> None:
        """Function to multiply the calculator's vector by a scalar"""
        self.vector = [value * scalar for value in self.vector]
        print(self.vector)

    def __sub__(self, scalar: float) -> None:
        """Function to subtract a scalar from the calculator's vector"""
        self.vector = [value - scalar for value in self.vector]
        print(self.vector)

    def __truediv__(self, scalar: float) -> None:
        """Function to divide the calculator's vector by a scalar"""
        if scalar == 0:
            print("Error: Division by zero is not allowed.")
            return
        self.vector = [value / scalar for value in self.vector]
        print(self.vector)


def main():
    """
    Reproduce the subject's tester.py: build calculator vectors
    and trigger +, *, - and / with a scalar. Note there is no
    print() around these calls - each dunder method has to
    print its own result.
    """
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5


if __name__ == "__main__":
    main()
