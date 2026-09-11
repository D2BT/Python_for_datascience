import pandas as pd
import matplotlib.pyplot as plt

from load_csv import load


def merge_gdp_life(
    income_df: pd.DataFrame,
    life_df: pd.DataFrame,
    year: str,
) -> pd.DataFrame:
    """
    Merge income_df and life_df on "country", keeping only that
    year's GDP and life expectancy values, so each row lines up
    the right country's two figures for the same year. Only
    countries present in both datasets are kept. Handle any
    error (wrong type, missing year column...) with a clear
    message and return None instead of crashing.
    """
    try:
        if not isinstance(year, str):
            raise TypeError("Year must be a string.")
        if year not in income_df.columns or year not in life_df.columns:
            raise ValueError(f"Year {year} not found in one of the datasets.")
        merged_df = pd.merge(
            income_df[["country", year]],
            life_df[["country", year]],
            on="country",
            how="inner",
        )
        merged_df.columns = ["country", "gdp", "life_expectancy"]
        return merged_df
    except (OSError, TypeError, ValueError, pd.errors.ParserError) as e:
        print(f"merge_gdp_life: error: {e}")
        return None


def main():
    """
    Load income_per_person_gdppercapita_ppp_inflation_adjusted.csv
    and life_expectancy_years.csv with the load() function from
    ex00 (load_csv.py), merge them for the year 1900 with
    merge_gdp_life(), then display life expectancy against GDP
    for every country as a scatter plot. The subject's example
    uses a log scale on the GDP axis: title "1900", x axis
    "Gross domestic product" (log scale), y axis
    "Life Expectancy".
    """
    income_df = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
        )
    life_df = load("life_expectancy_years.csv")
    merged_df = merge_gdp_life(income_df, life_df, "1900")
    if merged_df is not None:
        merged_df = merged_df.dropna()
        plt.title("1900")
        plt.xscale("log")
        plt.scatter(merged_df["gdp"], merged_df["life_expectancy"])
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy")
        plt.show()


if __name__ == "__main__":
    main()
