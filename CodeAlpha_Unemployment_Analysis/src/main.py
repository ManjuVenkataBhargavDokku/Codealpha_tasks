"""
==============================================================
Project : Unemployment Analysis with Python
Internship : CodeAlpha Data Science Internship
Author : Manju Venkata Bhargav Dokku
==============================================================
"""

import os

from data_cleaning import (
    load_dataset,
    clean_dataset
)

from analysis import (
    dataset_summary,
    missing_values,
    state_analysis,
    monthly_analysis,
    covid_analysis,
    correlation_analysis,
    top_states_analysis,
    region_analysis,
    final_report
)

from visualization import (
    dataset_preview,
    plot_histogram,
    plot_boxplot,
    plot_state_unemployment,
    plot_monthly_trend,
    plot_covid_impact,
    plot_labour_participation,
    plot_heatmap,
    plot_correlation_matrix,
    plot_top10_states,
    plot_pie_chart,
    plot_line_chart,
    project_completed
)


def create_folders():
    """
    Create images folder if it doesn't exist.
    """
    os.makedirs("../images", exist_ok=True)


def banner():
    """
    Display project banner.
    """
    print("=" * 70)
    print("        UNEMPLOYMENT ANALYSIS WITH PYTHON")
    print("      CodeAlpha Data Science Internship")
    print("      Developed by Manju Venkata Bhargav Dokku")
    print("=" * 70)


def main():

    banner()

    create_folders()

    print("\nLoading Dataset...\n")

    file_path = "../dataset/Unemployment in India.csv"

    data = load_dataset(file_path)

    print("Dataset Loaded Successfully.")

    print("\n")

    print("=" * 70)
    print("DATASET SUMMARY")
    print("=" * 70)

    dataset_summary(data)

    print("\n")

    print("=" * 70)
    print("CHECKING MISSING VALUES")
    print("=" * 70)

    missing_values(data)

    print("\nCleaning Dataset...\n")

    data = clean_dataset(data)

    print("Dataset Cleaned Successfully.")

    print("\n")

    print("=" * 70)
    print("GENERATING DATASET PREVIEW")
    print("=" * 70)

    dataset_preview(data)

    print("\n")

    print("=" * 70)
    print("STATE ANALYSIS")
    print("=" * 70)

    state_analysis(data)

    print("\n")

    print("=" * 70)
    print("MONTHLY ANALYSIS")
    print("=" * 70)

    monthly_analysis(data)

    print("\n")

    print("=" * 70)
    print("COVID-19 IMPACT ANALYSIS")
    print("=" * 70)

    covid_analysis(data)

    print("\n")

    print("=" * 70)
    print("CORRELATION ANALYSIS")
    print("=" * 70)

    correlation_analysis(data)
    print("\n")

    print("=" * 70)
    print("TOP 10 STATES WITH HIGHEST UNEMPLOYMENT")
    print("=" * 70)

    top_states_analysis(data)

    print("\n")

    print("=" * 70)
    print("AREA WISE ANALYSIS")
    print("=" * 70)

    region_analysis(data)

    print("\n")

    print("=" * 70)
    print("GENERATING VISUALIZATIONS")
    print("=" * 70)

    dataset_preview(data)

    plot_histogram(data)

    plot_boxplot(data)

    plot_state_unemployment(data)

    plot_monthly_trend(data)

    plot_covid_impact(data)

    plot_labour_participation(data)

    plot_heatmap(data)

    plot_correlation_matrix(data)

    plot_top10_states(data)

    plot_pie_chart(data)

    plot_line_chart(data)

    project_completed()

    print("\n")

    print("=" * 70)
    print("FINAL REPORT")
    print("=" * 70)

    final_report(data)

    print("\n")

    print("=" * 70)
    print("PROJECT SUMMARY")
    print("=" * 70)

    print("✓ Dataset Loaded Successfully")
    print("✓ Dataset Summary Generated")
    print("✓ Missing Values Checked")
    print("✓ Dataset Cleaned Successfully")
    print("✓ State-wise Analysis Completed")
    print("✓ Monthly Trend Analysis Completed")
    print("✓ COVID-19 Analysis Completed")
    print("✓ Correlation Analysis Completed")
    print("✓ Top 10 States Analysis Completed")
    print("✓ Area-wise Analysis Completed")
    print("✓ All Visualizations Generated")
    print("✓ Final Report Generated")

    print("\nGenerated Images")

    print("-" * 50)

    image_files = [
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

    for image in image_files:
        print(f"✓ {image}")

    print("-" * 50)

    print("\nProject Developed By")
    print("Manju Venkata Bhargav Dokku")

    print("\nCodeAlpha Data Science Internship")

    print("\nPROJECT COMPLETED SUCCESSFULLY")

    print("=" * 70)


if __name__ == "__main__":
    main()