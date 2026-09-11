import pandas as pd
import matplotlib.pyplot as plt

from load_csv import load


def aff_life(country: str, df: pd.DataFrame):
    """
    Filter df to keep only the row whose "country" is country.
    Handle any error (wrong type...) with a clear message and
    return None instead of crashing.
    """
    try:
        if not isinstance(country, str):
            raise TypeError("Country must be a string.")
        df = df[df["country"] == country]
        return df
    except (OSError, TypeError, pd.errors.ParserError) as e:
        print(f"aff_life: error: {e}")
        return None


def main():
    """
    Load life_expectancy_years.csv with the load() function from
    ex00 (load_csv.py), then display the life expectancy
    projection curve for your campus's country. The plot must
    have a title and a legend for each axis, matching the
    subject's example for a 42 France campus: title "France Life
    expectancy Projections", x axis "Year", y axis
    "Life expectancy" (adapt the country to your own campus).
    """
    df = load("life_expectancy_years.csv")
    country_df = aff_life("France", df)
    if country_df is not None:
        country_df = country_df.drop(columns=["country"])
        country_df = country_df.transpose()
        country_df.index = country_df.index.astype(int)
        country_df.columns = ["Life expectancy"]
        country_df.index.name = "Year"
        country_df.plot(
            title="France Life expectancy Projections",
            legend=False,
            )
        plt.xticks(range(1800, 2101, 40))
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()


if __name__ == "__main__":
    main()
