from S1E9 import Character


class Baratheon(Character):
    """A character belonging to House Baratheon."""

    def __init__(self, first_name, is_alive=True):
        """
        Set up a Baratheon: call Character's constructor for
        first_name/is_alive, then set the family's own
        attributes (family_name, eyes, hairs).
        """
        # your code here: call Character's __init__ (super()),
        # then set family_name="Baratheon", eyes="brown",
        # hairs="dark"
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Set is_alive to False."""
        super().die()  # call parent's die() (super())

    def __str__(self):
        """
        Return a short, human-readable string describing this
        Baratheon (must be an actual string, not an object).
        """
        return (
            f"{self.first_name} {self.family_name}, "
            f"Eyes: {self.eyes}, Hairs: {self.hairs}, "
            f"Alive: {self.is_alive}"
        )

    def __repr__(self):
        """
        Return an unambiguous string representation of this
        Baratheon (must be an actual string, not an object).
        """
        return (
            f"Baratheon(first_name={self.first_name!r}, "
            f"is_alive={self.is_alive!r})"
        )


class Lannister(Character):
    """A character belonging to House Lannister."""

    def __init__(self, first_name, is_alive=True):
        """
        Set up a Lannister: call Character's constructor for
        first_name/is_alive, then set the family's own
        attributes (family_name, eyes, hairs).
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Set is_alive to False."""
        super().die()  # call parent's die() (super())

    def __str__(self):
        """
        Return a short, human-readable string describing this
        Lannister (must be an actual string, not an object).
        """
        return (
            f"{self.first_name} {self.family_name}, "
            f"Eyes: {self.eyes}, Hairs: {self.hairs}, "
            f"Alive: {self.is_alive}"
        )

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Build and return a new Lannister, so a Lannister can be
        created via Lannister.create_lannister(...) instead of
        calling Lannister(...) directly.
        """
        return cls(first_name, is_alive)


def main():
    """
    Reproduce the subject's tester.py for S1E7: create a
    Baratheon and a Lannister, inspect their attributes, str()/
    repr()/doc, die(), then build a Lannister with the
    create_lannister() class method.
    """
    robert = Baratheon("Robert")
    print(robert.__dict__)
    print(robert.__str__())
    print(robert.__repr__())
    print(robert.is_alive)
    robert.die()
    print(robert.is_alive)
    print(robert.__doc__)
    print("---")
    cersei = Lannister("Cersei")
    print(cersei.__dict__)
    print(cersei.__str__())
    print(cersei.is_alive)
    print("---")
    jaine = Lannister.create_lannister("Jaine", True)
    print(
        f"Name : {jaine.first_name, type(jaine).__name__}, "
        f"Alive : {jaine.is_alive}"
    )


if __name__ == "__main__":
    main()
