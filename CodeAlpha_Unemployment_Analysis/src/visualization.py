"""
==============================================================
Project : Unemployment Analysis with Python
Internship : CodeAlpha Data Science Internship
Author : Manju Venkata Bhargav Dokku
==============================================================
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Create images folder
os.makedirs("../images", exist_ok=True)

sns.set_style("whitegrid")


def dataset_preview(data):
    """
    Save first 10 rows as an image.
    """

    fig, ax = plt.subplots(figsize=(14, 5))

    ax.axis("off")

    table = ax.table(
        cellText=data.head(10).values,
        colLabels=data.columns,
        loc="center"
    )

    table.auto_set_font_size(False)

    table.set_fontsize(8)

    table.scale(1.2, 1.6)

    plt.title("Dataset Preview")

    plt.savefig("../images/dataset_preview.png",
                dpi=300,
                bbox_inches="tight")

    plt.close()

    print("dataset_preview.png saved.")


def plot_histogram(data):
    """
    Histogram of unemployment rate
    """

    plt.figure(figsize=(10,6))

    sns.histplot(
        data["Estimated Unemployment Rate (%)"],
        bins=20,
        kde=True,
        color="royalblue"
    )

    plt.title("Distribution of Unemployment Rate")

    plt.xlabel("Unemployment Rate (%)")

    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig("../images/histogram.png",
                dpi=300)

    plt.close()

    print("histogram.png saved.")


def plot_boxplot(data):
    """
    Box Plot
    """

    plt.figure(figsize=(10,6))

    sns.boxplot(
        y=data["Estimated Unemployment Rate (%)"],
        color="orange"
    )

    plt.title("Box Plot of Unemployment Rate")

    plt.tight_layout()

    plt.savefig("../images/boxplot.png",
                dpi=300)

    plt.close()

    print("boxplot.png saved.")


def plot_state_unemployment(data):
    """
    Average unemployment by state
    """

    state = data.groupby("Region")[
        "Estimated Unemployment Rate (%)"
    ].mean().sort_values(ascending=False)

    plt.figure(figsize=(14,8))

    sns.barplot(
        x=state.values,
        y=state.index,
        palette="viridis"
    )

    plt.xlabel("Average Unemployment Rate (%)")

    plt.ylabel("State")

    plt.title("Average State-wise Unemployment Rate")

    plt.tight_layout()

    plt.savefig("../images/state_unemployment.png",
                dpi=300)

    plt.close()

    print("state_unemployment.png saved.")
def plot_monthly_trend(data):
    """
    Monthly unemployment trend
    """

    monthly = data.groupby("Month_Number")[
        "Estimated Unemployment Rate (%)"
    ].mean()

    month_names = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    plt.figure(figsize=(10,6))

    plt.plot(
        monthly.index,
        monthly.values,
        marker="o",
        linewidth=3,
        color="blue"
    )

    plt.xticks(range(1,13), month_names)

    plt.title("Monthly Unemployment Trend")

    plt.xlabel("Month")

    plt.ylabel("Average Unemployment Rate (%)")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "../images/monthly_trend.png",
        dpi=300
    )

    plt.close()

    print("monthly_trend.png saved.")


def plot_covid_impact(data):
    """
    COVID-19 impact visualization
    """

    before = data[data["Year"] < 2020]

    after = data[data["Year"] >= 2020]

    values = [
        before["Estimated Unemployment Rate (%)"].mean(),
        after["Estimated Unemployment Rate (%)"].mean()
    ]

    labels = [
        "Before COVID",
        "During COVID"
    ]

    plt.figure(figsize=(8,6))

    plt.bar(
        labels,
        values,
        color=["green", "red"]
    )

    plt.title("COVID-19 Impact on Unemployment")

    plt.ylabel("Average Unemployment Rate (%)")

    plt.tight_layout()

    plt.savefig(
        "../images/covid_impact.png",
        dpi=300
    )

    plt.close()

    print("covid_impact.png saved.")


def plot_labour_participation(data):
    """
    Labour Participation Trend
    """

    state = data.groupby("Region")[
        "Estimated Labour Participation Rate (%)"
    ].mean().sort_values()

    plt.figure(figsize=(14,8))

    plt.barh(
        state.index,
        state.values,
        color="teal"
    )

    plt.xlabel("Labour Participation Rate (%)")

    plt.ylabel("State")

    plt.title("State-wise Labour Participation Rate")

    plt.tight_layout()

    plt.savefig(
        "../images/labour_participation.png",
        dpi=300
    )

    plt.close()

    print("labour_participation.png saved.")


def plot_heatmap(data):
    """
    Correlation Heatmap
    """

    numeric = data.select_dtypes(include="number")

    plt.figure(figsize=(8,6))

    sns.heatmap(
        numeric.corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig(
        "../images/heatmap.png",
        dpi=300
    )

    plt.close()

    print("heatmap.png saved.")
def plot_correlation_matrix(data):
    """
    Correlation Matrix
    """

    numeric = data.select_dtypes(include="number")

    corr = numeric.corr()

    plt.figure(figsize=(8,6))

    sns.heatmap(
        corr,
        annot=True,
        cmap="YlGnBu",
        linewidths=0.5,
        fmt=".2f"
    )

    plt.title("Correlation Matrix")

    plt.tight_layout()

    plt.savefig(
        "../images/correlation_matrix.png",
        dpi=300
    )

    plt.close()

    print("correlation_matrix.png saved.")


def plot_top10_states(data):
    """
    Top 10 States with Highest Unemployment
    """

    top10 = (
        data.groupby("Region")
        ["Estimated Unemployment Rate (%)"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12,7))

    sns.barplot(
        x=top10.values,
        y=top10.index,
        palette="Reds_r"
    )

    plt.title("Top 10 States with Highest Unemployment")

    plt.xlabel("Average Unemployment Rate (%)")

    plt.ylabel("State")

    plt.tight_layout()

    plt.savefig(
        "../images/top10_states.png",
        dpi=300
    )

    plt.close()

    print("top10_states.png saved.")


def plot_pie_chart(data):
    """
    Top 5 States Pie Chart
    """

    top5 = (
        data.groupby("Region")
        ["Estimated Unemployment Rate (%)"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
    )

    plt.figure(figsize=(8,8))

    plt.pie(
        top5.values,
        labels=top5.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Top 5 States by Average Unemployment Rate")

    plt.tight_layout()

    plt.savefig(
        "../images/pie_chart.png",
        dpi=300
    )

    plt.close()

    print("pie_chart.png saved.")


def plot_line_chart(data):
    """
    Year-wise Average Unemployment Trend
    """

    yearly = (
        data.groupby("Year")
        ["Estimated Unemployment Rate (%)"]
        .mean()
    )

    plt.figure(figsize=(10,6))

    plt.plot(
        yearly.index,
        yearly.values,
        marker="o",
        linewidth=3
    )

    plt.title("Year-wise Average Unemployment Rate")

    plt.xlabel("Year")

    plt.ylabel("Average Unemployment Rate (%)")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "../images/yearly_trend.png",
        dpi=300
    )

    plt.close()

    print("yearly_trend.png saved.")


def project_completed():
    """
    Display completion message
    """

    print("\n" + "=" * 70)
    print("ALL VISUALIZATIONS GENERATED SUCCESSFULLY")
    print("=" * 70)

    print("\nImages saved inside '../images/' folder:\n")

    images = [
        "dataset_preview.png",
        "histogram.png",
        "boxplot.png",
        "state_unemployment.png",
        "monthly_trend.png",
        "covid_impact.png",
        "labour_participation.png",
        "heatmap.png",
        "correlation_matrix.png",
        "top10_states.png",
        "pie_chart.png",
        "yearly_trend.png"
    ]

    for image in images:
        print("✓", image)

    print("\nProject Completed Successfully.")