"""
==============================================================
Project : Unemployment Analysis with Python
Internship : CodeAlpha Data Science Internship
Author : Manju Venkata Bhargav Dokku
==============================================================
"""

import pandas as pd


def load_dataset(file_path):
    """
    Load the CSV dataset
    """

    try:

        data = pd.read_csv(file_path)

        print("Dataset loaded successfully.")

        return data

    except FileNotFoundError:

        print("Dataset not found.")

        exit()

    except Exception as e:

        print("Error:", e)

        exit()


def clean_dataset(data):
    """
    Perform complete data cleaning
    """

    print("\nCleaning Dataset...")

    # -----------------------------
    # Remove extra spaces from column names
    # -----------------------------

    data.columns = data.columns.str.strip()

    print("Column names cleaned.")

    # -----------------------------
    # Rename columns for convenience
    # -----------------------------

    data.rename(
        columns={
            " Region": "Region",
            " Date": "Date",
            " Frequency": "Frequency",
            " Estimated Unemployment Rate (%)":
                "Estimated Unemployment Rate (%)",
            " Estimated Employed":
                "Estimated Employed",
            " Estimated Labour Participation Rate (%)":
                "Estimated Labour Participation Rate (%)",
            " Area": "Area"
        },
        inplace=True
    )

    print("Columns renamed.")

    # -----------------------------
    # Remove duplicate rows
    # -----------------------------

    duplicates = data.duplicated().sum()

    print("\nDuplicate Rows :", duplicates)

    data.drop_duplicates(inplace=True)

    print("Duplicate rows removed.")

    # -----------------------------
    # Missing values
    # -----------------------------

    print("\nMissing Values")

    print(data.isnull().sum())

    # Remove missing values

    data.dropna(inplace=True)

    print("Missing values removed.")

    # -----------------------------
    # Reset Index
    # -----------------------------

    data.reset_index(drop=True, inplace=True)

    print("Index reset.")

    # -----------------------------
    # Convert Date column
    # -----------------------------

    if "Date" in data.columns:

        data["Date"] = pd.to_datetime(
            data["Date"],
            dayfirst=True,
            errors="coerce"
        )

        print("Date converted to datetime.")

    # -----------------------------
    # Remove rows with invalid dates
    # -----------------------------

    if "Date" in data.columns:

        data.dropna(subset=["Date"], inplace=True)

        print("Invalid dates removed.")

    # -----------------------------
    # Clean text columns
    # -----------------------------

    if "Region" in data.columns:

        data["Region"] = data["Region"].str.strip()

    if "Area" in data.columns:

        data["Area"] = data["Area"].str.strip()

    if "Frequency" in data.columns:

        data["Frequency"] = data["Frequency"].str.strip()

    print("Text columns cleaned.")
        # -----------------------------
    # Convert numerical columns
    # -----------------------------

    numeric_columns = [
        "Estimated Unemployment Rate (%)",
        "Estimated Employed",
        "Estimated Labour Participation Rate (%)"
    ]

    for column in numeric_columns:

        if column in data.columns:

            data[column] = pd.to_numeric(
                data[column],
                errors="coerce"
            )

    print("Numerical columns converted.")

    # -----------------------------
    # Remove invalid numeric values
    # -----------------------------

    data.dropna(subset=numeric_columns, inplace=True)

    print("Invalid numeric values removed.")

    # -----------------------------
    # Create Year Column
    # -----------------------------

    if "Date" in data.columns:

        data["Year"] = data["Date"].dt.year

        print("Year column created.")

    # -----------------------------
    # Create Month Column
    # -----------------------------

    if "Date" in data.columns:

        data["Month"] = data["Date"].dt.month_name()

        print("Month column created.")

    # -----------------------------
    # Create Month Number
    # -----------------------------

    if "Date" in data.columns:

        data["Month_Number"] = data["Date"].dt.month

        print("Month Number column created.")

    # -----------------------------
    # Sort Dataset
    # -----------------------------

    if "Date" in data.columns:

        data.sort_values(
            by="Date",
            inplace=True
        )

        print("Dataset sorted by Date.")

    # -----------------------------
    # Reset Index Again
    # -----------------------------

    data.reset_index(
        drop=True,
        inplace=True
    )

    print("Index reset successfully.")

    # -----------------------------
    # Dataset Shape
    # -----------------------------

    print("\nFinal Dataset Shape")

    print(data.shape)

    # -----------------------------
    # Data Types
    # -----------------------------

    print("\nData Types")

    print(data.dtypes)

    # -----------------------------
    # First Five Rows
    # -----------------------------

    print("\nFirst Five Rows")

    print(data.head())

    # -----------------------------
    # Last Five Rows
    # -----------------------------

    print("\nLast Five Rows")

    print(data.tail())

    # -----------------------------
    # Final Missing Values
    # -----------------------------

    print("\nMissing Values After Cleaning")

    print(data.isnull().sum())

    # -----------------------------
    # Statistical Summary
    # -----------------------------

    print("\nStatistical Summary")

    print(data.describe())

    # -----------------------------
    # Dataset Ready
    # -----------------------------

    print("\nDataset Ready For Analysis.")

    return data