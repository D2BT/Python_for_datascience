import sys


def check_building(val: str):
    """Count and print upper, lower, punctuation, space and digit chars."""
    upper = 0
    lower = 0
    digit = 0
    punctuation = 0
    space = 0
    for i in range(len(val)):
        if val[i].isupper():
            upper += 1
        elif val[i].islower():
            lower += 1
        elif val[i].isdigit():
            digit += 1
        elif val[i].isspace():
            space += 1
        else:
            punctuation += 1
    print("The text contains %d characters:" % len(val))
    print("%d upper letters" % upper)
    print("%d lower letters" % lower)
    print("%d punctuation marks" % punctuation)
    print("%d spaces" % space)
    print("%d digits" % digit)


def main():
    """Read a string from argv (or prompt for one) and count its chars."""
    if len(sys.argv) < 2:
        text = input("What is the text to count?\n")
        check_building(text)
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
    else:
        check_building(sys.argv[1])


if __name__ == "__main__":
    main()
