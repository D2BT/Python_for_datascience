class calculator:
    """
    A calculator working on two vectors of the same size, where
    every operation (dot product, addition, subtraction) is
    available directly on the class itself - thanks to
    @staticmethod, no instance ever needs to be created.
    """

    @staticmethod
    def dotproduct(v1: list[float], v2: list[float]) -> None:
        """
        Compute the dot product of v1 and v2 (the sum of each
        pair of matching elements multiplied together), then
        print it as "Dot product is: <value>".
        """
        print(f"Dot product is: {sum(a * b for a, b in zip(v1, v2))}")

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        """
        Compute the element-wise sum of v1 and v2 as a list of
        floats, then print it as "Add Vector is : [...]".
        """
        print(f"Add Vector is : {[float(a + b) for a, b in zip(v1, v2)]}")

    @staticmethod
    def sous_vec(v1: list[float], v2: list[float]) -> None:
        """
        Compute the element-wise subtraction of v2 from v1
        (v1 - v2) as a list of floats, then print it as
        "Sous Vector is: [...]".
        """
        print(f"Sous Vector is: {[float(a - b) for a, b in zip(v1, v2)]}")


def main():
    """
    Reproduce the subject's tester.py: call calculator's methods
    directly on the class (no instance created, thanks to the
    decorator above each method), on two same-size vectors.
    """
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
