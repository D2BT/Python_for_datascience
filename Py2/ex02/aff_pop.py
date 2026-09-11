import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from load_csv import load


def aff_pop(country1: str, country2: str, df: pd.DataFrame):
    """
    Filter df to keep only the rows whose "country" is country1
    or country2. Handle any error (wrong type...) with a clear
    message and return None instead of crashing.
    """
    try:
        if not isinstance(country1, str) or not isinstance(country2, str):
            raise TypeError("Country must be strings.")
        df = df[df["country"].isin([country1, country2])]
        return df
    except (OSError, TypeError, pd.errors.ParserError) as e:
        print(f"aff_pop: error: {e}")
        return None


def parse_population(value: str) -> float:
    """Convert a Gapminder-style population string ("64.7M",
    "76.1k"...) into a plain float."""
    multipliers = {"k": 1_000, "M": 1_000_000, "B": 1_000_000_000}
    if value[-1] in multipliers:
        return float(value[:-1]) * multipliers[value[-1]]
    return float(value)


def format_population(value, _):
    """
    Matplotlib tick formatter: turn a raw population value (e.g.
    20000000.0) back into a Gapminder-style short label (e.g.
    "20M"), so the Y axis reads like the CSV instead of using
    matplotlib's default scientific notation (a tiny "1e7" off
    to the side).
    """
    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:g}B"
    if value >= 1_000_000:
        return f"{value / 1_000_000:g}M"
    if value >= 1_000:
        return f"{value / 1_000:g}k"
    return f"{value:g}"


def main():
    """
    Load population_total.csv with the load() function from ex00
    (load_csv.py), then display the population projection curves
    (years 1800 to 2050) for your campus's country (France) and
    another country of your choice (Belgium), converting the
    Gapminder-style population strings to plain numbers with
    parse_population(). The plot has a title, a legend for each
    axis, and a legend distinguishing each curve.
    """
    df = load("population_total.csv")
    country_df = aff_pop("France", "Belgium", df)
    if country_df is not None:
        country_df = country_df.set_index("country")
        country_df = country_df.transpose()
        country_df.index = country_df.index.astype(int)
        country_df = country_df.loc[1800:2050]
        country_df["France"] = country_df["France"].apply(parse_population)
        country_df["Belgium"] = country_df["Belgium"].apply(parse_population)
        country_df.index.name = "Year"
        ax = country_df.plot(
            title="Population projections",
            legend=True,
            )
        ax.yaxis.set_major_formatter(FuncFormatter(format_population))
        plt.xticks(range(1800, 2050, 40))
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.show()


if __name__ == "__main__":
    main()
