"""
===========================================================
Project : Unemployment Analysis with Python
Internship : CodeAlpha Data Science Internship
Author : Manju Venkata Bhargav Dokku
===========================================================
"""

import pandas as pd


def dataset_summary(df):
    """
    Display dataset information
    """

    print("\nFirst Five Rows\n")
    print(df.head())

    print("\nLast Five Rows\n")
    print(df.tail())

    print("\nDataset Shape")
    print(df.shape)

    print("\nColumn Names")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nDataset Information")
    df.info()

    print("\nStatistical Summary")
    print(df.describe(include="all"))


def missing_values(df):
    """
    Check missing values
    """

    print("\nMissing Values")

    missing = df.isnull().sum()

    print(missing)

    if missing.sum() == 0:
        print("\nNo Missing Values Found.")
    else:
        print("\nMissing Values Detected.")


def state_analysis(df):
    """
    State-wise unemployment analysis
    """

    print("\nAverage Unemployment Rate by State\n")

    state_avg = (
        df.groupby("Region")["Estimated Unemployment Rate (%)"]
        .mean()
        .sort_values(ascending=False)
    )

    print(state_avg)

    print("\nHighest Unemployment State")

    highest = state_avg.idxmax()

    print(highest)

    print("\nRate")

    print(round(state_avg.max(), 2), "%")

    print("\nLowest Unemployment State")

    lowest = state_avg.idxmin()

    print(lowest)

    print("\nRate")

    print(round(state_avg.min(), 2), "%")


def monthly_analysis(df):
    """
    Monthly unemployment trend
    """

    if "Date" not in df.columns:
        print("Date column not found.")
        return

    print("\nMonthly Average Unemployment\n")

    monthly = (
        df.groupby(df["Date"].dt.month_name())
        ["Estimated Unemployment Rate (%)"]
        .mean()
    )

    print(monthly)

    highest_month = monthly.idxmax()

    lowest_month = monthly.idxmin()

    print("\nHighest Unemployment Month")

    print(highest_month)

    print("\nAverage Rate")

    print(round(monthly.max(), 2), "%")

    print("\nLowest Unemployment Month")

    print(lowest_month)

    print("\nAverage Rate")

    print(round(monthly.min(), 2), "%")


def covid_analysis(df):
    """
    Compare unemployment before and during COVID-19
    """

    if "Date" not in df.columns:
        print("Date column not found.")
        return

    before = df[df["Date"] < "2020-03-01"]

    after = df[df["Date"] >= "2020-03-01"]

    before_rate = before["Estimated Unemployment Rate (%)"].mean()

    after_rate = after["Estimated Unemployment Rate (%)"].mean()

    print("\nCOVID-19 Impact Analysis")

    print("\nAverage Before COVID")

    print(round(before_rate, 2), "%")

    print("\nAverage During COVID")

    print(round(after_rate, 2), "%")

    difference = after_rate - before_rate

    print("\nIncrease")

    print(round(difference, 2), "%")
def correlation_analysis(df):
    """
    Display correlation between numerical columns
    """

    numeric_df = df.select_dtypes(include=["number"])

    correlation = numeric_df.corr()

    print("\nCorrelation Matrix\n")
    print(correlation)

    print("\nKey Insights\n")

    unemployment = "Estimated Unemployment Rate (%)"
    employed = "Estimated Employed"
    labour = "Estimated Labour Participation Rate (%)"

    if unemployment in correlation.columns:

        print(
            f"Correlation between Unemployment and Employment : "
            f"{round(correlation.loc[unemployment, employed], 3)}"
        )

        print(
            f"Correlation between Unemployment and Labour Participation : "
            f"{round(correlation.loc[unemployment, labour], 3)}"
        )

        if correlation.loc[unemployment, employed] < 0:
            print("\nHigher unemployment generally means fewer employed people.")

        if correlation.loc[unemployment, labour] > 0:
            print("Higher labour participation may increase unemployment temporarily.")
        else:
            print("Labour participation has an inverse relationship with unemployment.")


def top_states_analysis(df):
    """
    Display Top 10 states with highest unemployment
    """

    top_states = (
        df.groupby("Region")["Estimated Unemployment Rate (%)"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    print(top_states)

    print("\nHighest Unemployment State")

    print(top_states.index[0])

    print("Average Rate :", round(top_states.iloc[0], 2), "%")

    print("\nLowest Among Top 10")

    print(top_states.index[-1])

    print("Average Rate :", round(top_states.iloc[-1], 2), "%")

    print("\nRanking")

    for i, (state, value) in enumerate(top_states.items(), start=1):

        print(
            f"{i}. {state:<25} {round(value,2)} %"
        )


def region_analysis(df):

    if "Area" not in df.columns:
        print("\nArea column not available in this dataset.")
        return

    print("\nArea-wise Unemployment Analysis\n")

    area = (
        df.groupby("Area")["Estimated Unemployment Rate (%)"]
        .mean()
        .sort_values(ascending=False)
    )

    print(area)


def final_report(df):
    """
    Final Summary Report
    """

    average = df["Estimated Unemployment Rate (%)"].mean()

    maximum = df["Estimated Unemployment Rate (%)"].max()

    minimum = df["Estimated Unemployment Rate (%)"].min()

    print(f"\nAverage Unemployment Rate : {average:.2f}%")

    print(f"Maximum Unemployment Rate : {maximum:.2f}%")

    print(f"Minimum Unemployment Rate : {minimum:.2f}%")

    state = (
        df.groupby("Region")["Estimated Unemployment Rate (%)"]
        .mean()
        .idxmax()
    )

    print(f"\nMost Affected State : {state}")

    print("\nAnalysis Completed Successfully.")

    print("=" * 70)