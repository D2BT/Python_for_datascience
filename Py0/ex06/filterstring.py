import sys
from ft_filter import ft_filter


def main():
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")

    try:
        chaine = sys.argv[1]

        limite = int(sys.argv[2])
        if chaine.isdigit():
            raise AssertionError("the arguments are bad")

    except ValueError:
        raise AssertionError("the arguments are bad")

    mots = chaine.split()

    filtre_iterable = ft_filter(lambda mot: len(mot) > limite, mots)

    resultat = [mot for mot in filtre_iterable]

    print(resultat)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
