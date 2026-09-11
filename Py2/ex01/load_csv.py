import pandas as pd


def load(path: str):
    """
    Load the dataset at path, print its dimensions in the format
    "Loading dataset of dimensions (rows, cols)", and return it
    (a pandas DataFrame, or whatever type your library uses).
    Handle any error (missing file, wrong path, bad format...)
    with a clear message and return None instead of crashing.
    """
    try:
        if not isinstance(path, str):
            raise TypeError("Path must be a string.")
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions ({df.shape[0]}, {df.shape[1]})")
        return df
    except (OSError, TypeError, pd.errors.ParserError) as e:
        print(f"load: error: {e}")
        return None


def main():
    """Call load on life_expectancy_years.csv and print the result."""
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
