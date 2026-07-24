"""
===========================================================
Sales Prediction using Machine Learning
Visualization Module

Author : Manju Venkata Bhargav Dokku
===========================================================
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns

# Create images folder if it doesn't exist
os.makedirs("../images", exist_ok=True)

# ===========================================================
# Dataset Preview
# ===========================================================

def dataset_preview(data):

    fig, ax = plt.subplots(figsize=(12,4))

    ax.axis("off")

    table = ax.table(
        cellText=data.head(10).values,
        colLabels=data.columns,
        cellLoc="center",
        loc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.5)

    plt.title("Dataset Preview")

    plt.savefig("../images/dataset_preview.png",
                dpi=300,
                bbox_inches="tight")

    plt.close()


# ===========================================================
# Sales Distribution
# ===========================================================

def sales_distribution(data):

    plt.figure(figsize=(8,5))

    sns.histplot(
        data["Sales"],
        bins=20,
        kde=True,
        color="royalblue"
    )

    plt.title("Sales Distribution")
    plt.xlabel("Sales")
    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig("../images/sales_distribution.png",
                dpi=300)

    plt.close()


# ===========================================================
# Correlation Heatmap
# ===========================================================

def correlation_heatmap(data):

    plt.figure(figsize=(8,6))

    sns.heatmap(
        data.corr(),
        annot=True,
        cmap="coolwarm",
        linewidths=0.5
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig("../images/correlation_heatmap.png",
                dpi=300)

    plt.close()


# ===========================================================
# TV vs Sales
# ===========================================================

def tv_vs_sales(data):

    plt.figure(figsize=(8,5))

    sns.scatterplot(
        x="TV",
        y="Sales",
        data=data,
        color="blue"
    )

    plt.title("TV Advertising vs Sales")

    plt.tight_layout()

    plt.savefig("../images/tv_vs_sales.png",
                dpi=300)

    plt.close()


# ===========================================================
# Radio vs Sales
# ===========================================================

def radio_vs_sales(data):

    plt.figure(figsize=(8,5))

    sns.scatterplot(
        x="Radio",
        y="Sales",
        data=data,
        color="green"
    )

    plt.title("Radio Advertising vs Sales")

    plt.tight_layout()

    plt.savefig("../images/radio_vs_sales.png",
                dpi=300)

    plt.close()


# ===========================================================
# Newspaper vs Sales
# ===========================================================

def newspaper_vs_sales(data):

    plt.figure(figsize=(8,5))

    sns.scatterplot(
        x="Newspaper",
        y="Sales",
        data=data,
        color="red"
    )

    plt.title("Newspaper Advertising vs Sales")

    plt.tight_layout()

    plt.savefig("../images/newspaper_vs_sales.png",
                dpi=300)

    plt.close()


# ===========================================================
# Feature Importance
# ===========================================================

def feature_importance(model, feature_names):

    importance = model.feature_importances_

    plt.figure(figsize=(8,5))

    sns.barplot(
        x=importance,
        y=feature_names
    )

    plt.title("Feature Importance")

    plt.xlabel("Importance Score")
    plt.ylabel("Features")

    plt.tight_layout()

    plt.savefig("../images/feature_importance.png",
                dpi=300)

    plt.close()


# ===========================================================
# Actual vs Predicted
# ===========================================================

def actual_vs_predicted(y_test, predictions):

    plt.figure(figsize=(7,7))

    plt.scatter(
        y_test,
        predictions
    )

    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        "r--"
    )

    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")

    plt.title("Actual vs Predicted Sales")

    plt.tight_layout()

    plt.savefig("../images/actual_vs_predicted.png",
                dpi=300)

    plt.close()


# ===========================================================
# Residual Plot
# ===========================================================

def residual_plot(y_test, predictions):

    residuals = y_test - predictions

    plt.figure(figsize=(8,5))

    sns.scatterplot(
        x=predictions,
        y=residuals
    )

    plt.axhline(
        y=0,
        color="red",
        linestyle="--"
    )

    plt.xlabel("Predicted Sales")
    plt.ylabel("Residuals")

    plt.title("Residual Plot")

    plt.tight_layout()

    plt.savefig("../images/residual_plot.png",
                dpi=300)

    plt.close()


# ===========================================================
# Generate All Graphs
# ===========================================================

def generate_visualizations(data):

    dataset_preview(data)

    sales_distribution(data)

    correlation_heatmap(data)

    tv_vs_sales(data)

    radio_vs_sales(data)

    newspaper_vs_sales(data)

    print("\nAll visualizations generated successfully.")