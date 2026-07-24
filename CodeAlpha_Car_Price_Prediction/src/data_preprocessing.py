"""
==============================================================
Project : Car Price Prediction using Machine Learning
Internship : CodeAlpha Data Science Internship
Author : Manju Venkata Bhargav Dokku
==============================================================
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
def load_dataset(file_path):
    """
    Load the dataset from CSV.
    """

    data = pd.read_csv(file_path)

    print("=" * 60)
    print("DATASET LOADED SUCCESSFULLY")
    print("=" * 60)

    return data
def dataset_information(data):
    """
    Display dataset information.
    """

    print("\nFirst 10 Rows\n")
    print(data.head(10))

    print("\nDataset Shape\n")
    print(data.shape)

    print("\nColumn Names\n")
    print(data.columns.tolist())

    print("\nData Types\n")
    print(data.dtypes)

    print("\nDataset Information\n")
    data.info()

    print("\nStatistical Summary\n")
    print(data.describe())
def check_missing_values(data):
    """
    Check missing values.
    """

    print("\nMissing Values\n")

    print(data.isnull().sum())
def remove_duplicates(data):
    """
    Remove duplicate records.
    """

    duplicates = data.duplicated().sum()

    print("\nDuplicate Records :", duplicates)

    data = data.drop_duplicates()

    print("Duplicates Removed Successfully")

    return data
def create_car_age(data):
    """
    Create Car Age feature.
    """

    current_year = 2026

    data["Car_Age"] = current_year - data["Year"]

    print("\nCar Age Feature Created Successfully")

    return data
def drop_year_column(data):
    """
    Drop Year column.
    """

    data = data.drop("Year", axis=1)

    print("\nYear Column Removed")

    return data
def encode_data(data):
    """
    Encode categorical columns.
    """

    encoder = LabelEncoder()

    categorical_columns = [
        "Car_Name",
        "Fuel_Type",
        "Selling_type",
        "Transmission"
    ]

    for column in categorical_columns:
        data[column] = encoder.fit_transform(data[column])

    print("\nCategorical Columns Encoded Successfully")

    return data
def split_features_target(data):
    """
    Split features and target.
    """

    X = data.drop("Selling_Price", axis=1)

    y = data["Selling_Price"]

    return X, y
def clean_dataset(data):
    """
    Complete preprocessing pipeline.
    """

    check_missing_values(data)

    data = remove_duplicates(data)

    data = create_car_age(data)

    data = drop_year_column(data)

    data = encode_data(data)

    return data
