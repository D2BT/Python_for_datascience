from abc import ABC, abstractmethod


class Character(ABC):
    """A base class representing a Game of Thrones character."""

    def __init__(self, first_name, is_alive=True):
        """Set the character's first name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Set is_alive to False."""


class Stark(Character):
    """A character belonging to House Stark."""

    def die(self):
        """Set is_alive to False."""
        self.is_alive = False


def main():
    """
    Reproduce the subject's tester.py: create a Stark, inspect
    its __dict__ / is_alive / die() / docstrings, then create a
    second Stark directly with is_alive=False.
    """
    ned = Stark("Ned")
    print(ned.__dict__)
    print(ned.is_alive)
    ned.die()
    print(ned.is_alive)
    print(ned.__doc__)
    print(ned.__init__.__doc__)
    print(ned.die.__doc__)
    print("---")
    lyanna = Stark("Lyanna", False)
    print(lyanna.__dict__)


if __name__ == "__main__":
    main()
