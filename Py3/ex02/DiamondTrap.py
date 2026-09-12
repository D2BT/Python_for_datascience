from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A character belonging to the house Baratheon and Lannister."""

    def get_eyes(self):
        """Function to get the eyes of the King"""
        return self.eyes

    def set_eyes(self, eyes):
        """Function to set the eyes of the King"""
        self.eyes = eyes

    def get_hairs(self):
        """Function to get the hairs of the King"""
        return self.hairs

    def set_hairs(self, hairs):
        """Function to set the hairs of the King"""
        self.hairs = hairs


def main():
    """
    Reproduce the subject's tester.py for DiamondTrap: create a
    King (using multiple inheritance from Baratheon and
    Lannister - this is the "diamond" the subject's info box
    talks about, since both already inherit from Character;
    Python's C3 linearization decides the method resolution
    order), then change his eyes/hairs and check the result.
    """
    joffrey = King("Joffrey")
    print(joffrey.__dict__)
    joffrey.set_eyes("blue")
    joffrey.set_hairs("light")
    print(joffrey.get_eyes())
    print(joffrey.get_hairs())
    print(joffrey.__dict__)


if __name__ == "__main__":
    main()
