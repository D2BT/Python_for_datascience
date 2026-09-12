import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Function to generate a random id."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A student with a name, surname, login and id."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Function to compute login and id after init."""
        self.login = self.name[0].upper() + self.surname
        self.id = generate_id()


def main():
    """Function to test the Student class."""
    student = Student(name="Edward", surname="agle")
    print(student)


if __name__ == "__main__":
    main()
