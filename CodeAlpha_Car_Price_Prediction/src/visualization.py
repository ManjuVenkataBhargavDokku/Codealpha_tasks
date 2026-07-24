"""
==============================================================
Project : Car Price Prediction using Machine Learning
Internship : CodeAlpha Data Science Internship
Author : Manju Venkata Bhargav Dokku
==============================================================
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create images folder
os.makedirs("../images", exist_ok=True)

# Set plot style
sns.set_style("whitegrid")


def dataset_preview(data):
    """
    Save dataset preview as an image.
    """

    fig, ax = plt.subplots(figsize=(15, 5))

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

    plt.savefig(
        "../images/dataset_preview.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print("dataset_preview.png saved.")


def price_distribution(data):
    """
    Distribution of selling price.
    """

    plt.figure(figsize=(10, 6))

    sns.histplot(
        data["Selling_Price"],
        bins=30,
        kde=True,
        color="royalblue"
    )

    plt.title("Selling Price Distribution")

    plt.xlabel("Selling Price (Lakhs)")
    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig(
        "../images/price_distribution.png",
        dpi=300
    )

    plt.close()

    print("price_distribution.png saved.")


def box_plot(data):
    """
    Box plot of selling price.
    """

    plt.figure(figsize=(8, 6))

    sns.boxplot(
        y=data["Selling_Price"],
        color="orange"
    )

    plt.title("Selling Price Box Plot")

    plt.tight_layout()

    plt.savefig(
        "../images/boxplot.png",
        dpi=300
    )

    plt.close()

    print("boxplot.png saved.")


def correlation_heatmap(data):
    """
    Correlation heatmap.
    """

    plt.figure(figsize=(10, 8))

    sns.heatmap(
        data.corr(numeric_only=True),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig(
        "../images/correlation_heatmap.png",
        dpi=300
    )

    plt.close()

    print("correlation_heatmap.png saved.")
def brand_analysis(data):
    """
    Average selling price by car brand.
    """

    brand_price = (
        data.groupby("Car_Name")["Selling_Price"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12,6))

    sns.barplot(
        x=brand_price.index,
        y=brand_price.values,
        palette="viridis"
    )

    plt.xticks(rotation=45)

    plt.title("Top 10 Car Brands by Average Selling Price")

    plt.xlabel("Car Brand")

    plt.ylabel("Average Selling Price (Lakhs)")

    plt.tight_layout()

    plt.savefig(
        "../images/brand_analysis.png",
        dpi=300
    )

    plt.close()

    print("brand_analysis.png saved.")


def fuel_type_distribution(data):
    """
    Fuel Type Distribution
    """

    plt.figure(figsize=(8,6))

    sns.countplot(
        x="Fuel_Type",
        data=data,
        palette="Set2"
    )

    plt.title("Fuel Type Distribution")

    plt.xlabel("Fuel Type")

    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig(
        "../images/fuel_type.png",
        dpi=300
    )

    plt.close()

    print("fuel_type.png saved.")


def transmission_distribution(data):
    """
    Transmission Distribution
    """

    plt.figure(figsize=(8,6))

    sns.countplot(
        x="Transmission",
        data=data,
        palette="Set3"
    )

    plt.title("Transmission Distribution")

    plt.xlabel("Transmission")

    plt.ylabel("Number of Cars")

    plt.tight_layout()

    plt.savefig(
        "../images/transmission.png",
        dpi=300
    )

    plt.close()

    print("transmission.png saved.")


def owner_distribution(data):
    """
    Owner Distribution
    """

    plt.figure(figsize=(8,6))

    sns.countplot(
        x="Owner",
        data=data,
        palette="Pastel1"
    )

    plt.title("Owner Distribution")

    plt.xlabel("Previous Owners")

    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig(
        "../images/owner_distribution.png",
        dpi=300
    )

    plt.close()

    print("owner_distribution.png saved.")


def car_age_distribution(data):
    """
    Distribution of Car Age
    """

    plt.figure(figsize=(10,6))

    sns.histplot(
        data["Car_Age"],
        bins=20,
        kde=True,
        color="green"
    )

    plt.title("Car Age Distribution")

    plt.xlabel("Car Age (Years)")

    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig(
        "../images/car_age_distribution.png",
        dpi=300
    )

    plt.close()

    print("car_age_distribution.png saved.")

def actual_vs_predicted(y_test, predictions):
    """
    Plot Actual vs Predicted Prices
    """

    plt.figure(figsize=(8,8))

    plt.scatter(
        y_test,
        predictions,
        color="royalblue",
        alpha=0.7
    )

    minimum = min(min(y_test), min(predictions))
    maximum = max(max(y_test), max(predictions))

    plt.plot(
        [minimum, maximum],
        [minimum, maximum],
        color="red",
        linewidth=2
    )

    plt.xlabel("Actual Selling Price")

    plt.ylabel("Predicted Selling Price")

    plt.title("Actual vs Predicted Selling Price")

    plt.tight_layout()

    plt.savefig(
        "../images/actual_vs_predicted.png",
        dpi=300
    )

    plt.close()

    print("actual_vs_predicted.png saved.")


def residual_plot(y_test, predictions):
    """
    Residual Plot
    """

    residuals = y_test - predictions

    plt.figure(figsize=(10,6))

    plt.scatter(
        predictions,
        residuals,
        color="green",
        alpha=0.7
    )

    plt.axhline(
        y=0,
        color="red",
        linestyle="--"
    )

    plt.xlabel("Predicted Price")

    plt.ylabel("Residuals")

    plt.title("Residual Plot")

    plt.tight_layout()

    plt.savefig(
        "../images/residual_plot.png",
        dpi=300
    )

    plt.close()

    print("residual_plot.png saved.")


def project_completed():
    """
    Display completion message.
    """

    print("\n" + "=" * 70)
    print("ALL VISUALIZATIONS GENERATED SUCCESSFULLY")
    print("=" * 70)

    print("\nImages saved in the 'images' folder:\n")

    images = [
        "dataset_preview.png",
        "price_distribution.png",
        "boxplot.png",
        "correlation_heatmap.png",
        "brand_analysis.png",
        "fuel_type.png",
        "transmission.png",
        "owner_distribution.png",
        "car_age_distribution.png",
        "feature_importance.png",
        "actual_vs_predicted.png",
        "residual_plot.png"
    ]

    for image in images:
        print("✓", image)

    print("\nVisualization Module Completed Successfully.")