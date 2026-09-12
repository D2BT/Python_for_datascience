from typing import Any


def ft_percentile(data: tuple, p: float) -> float:
    """Function to compute the p-th percentile of data by hand."""
    sorted_data = sorted(data)
    n = len(sorted_data)
    rank = (p / 100) * (n - 1)
    lower = int(rank)
    upper = min(lower + 1, n - 1)
    fraction = rank - lower
    return sorted_data[lower] + fraction * (
        sorted_data[upper] - sorted_data[lower]
    )


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Function to print the statistics asked for in kwargs."""
    for stat in kwargs.values():
        try:
            if not args:
                raise ValueError("no data to compute statistics on")
            if stat == "mean":
                print(f"mean : {sum(args) / len(args)}")
            elif stat == "median":
                sorted_args = sorted(args)
                n = len(sorted_args)
                mid = n // 2
                if n % 2 == 1:
                    median = sorted_args[mid]
                else:
                    median = (
                        sorted_args[mid - 1] + sorted_args[mid]
                    ) / 2
                print(f"median : {median}")
            elif stat == "quartile":
                q1 = ft_percentile(args, 25)
                q3 = ft_percentile(args, 75)
                print(f"quartile : [{q1}, {q3}]")
            elif stat == "std":
                mean = sum(args) / len(args)
                variance = sum((x - mean) ** 2 for x in args) / len(args)
                print(f"std : {variance ** 0.5}")
            elif stat == "var":
                mean = sum(args) / len(args)
                variance = sum((x - mean) ** 2 for x in args) / len(args)
                print(f"var : {variance}")
        except (ZeroDivisionError, ValueError, IndexError):
            print("ERROR")


def main():
    """Function to test ft_statistics with different inputs."""
    ft_statistics(
        1, 42, 360, 11, 64,
        toto="mean", tutu="median", tata="quartile",
    )
    print("-----")
    ft_statistics(
        5, 75, 450, 18, 597, 27474, 48575,
        hello="std", world="var",
    )
    print("-----")
    ft_statistics(
        5, 75, 450, 18, 597, 27474, 48575,
        ejfhhe="heheh", ejdjdejn="kdekem",
    )
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
