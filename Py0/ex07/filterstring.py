import sys


def main():
    """Print words of S (argv[1]) longer than N (argv[2])."""
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")

    chaine = sys.argv[1]
    try:
        limite = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    mots = chaine.split()
    resultat = [mot for mot in filter(lambda mot: len(mot) > limite, mots)]
    print(resultat)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
