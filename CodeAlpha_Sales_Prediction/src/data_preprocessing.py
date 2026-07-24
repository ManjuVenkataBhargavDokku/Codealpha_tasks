"""
===========================================================
Sales Prediction using Machine Learning
Data Preprocessing Module

Author : Manju Venkata Bhargav Dokku
===========================================================
"""

import pandas as pd
from sklearn.model_selection import train_test_split


# ===========================================================
# Load Dataset
# ===========================================================

def load_dataset(file_path):
    """
    Load the dataset from CSV file.
    """

    data = pd.read_csv(file_path)
    # Remove unnecessary index column if present
    if "Unnamed: 0" in data.columns:
        data.drop("Unnamed: 0", axis=1, inplace=True)
    print("=" * 60)
    print("Dataset Loaded Successfully")
    print("=" * 60)

    return data


# ===========================================================
# Display Dataset Information
# ===========================================================

def dataset_information(data):

    print("\nFirst 10 Rows")
    print(data.head(10))

    print("\n" + "=" * 60)
    print("Dataset Information")
    print("=" * 60)

    print(data.info())

    print("\nDataset Shape")
    print(data.shape)

    print("\nColumn Names")
    print(data.columns.tolist())

    print("\nData Types")
    print(data.dtypes)


# ===========================================================
# Missing Values
# ===========================================================

def check_missing_values(data):

    print("\n" + "=" * 60)
    print("Missing Values")
    print("=" * 60)

    print(data.isnull().sum())


# ===========================================================
# Duplicate Values
# ===========================================================

def remove_duplicates(data):

    duplicates = data.duplicated().sum()

    print("\nDuplicate Rows :", duplicates)

    if duplicates > 0:

        data = data.drop_duplicates()

        print("Duplicate rows removed successfully.")

    else:

        print("No duplicate rows found.")

    return data


# ===========================================================
# Statistical Summary
# ===========================================================

def statistical_summary(data):

    print("\n" + "=" * 60)
    print("Statistical Summary")
    print("=" * 60)

    print(data.describe())


# ===========================================================
# Separate Features and Target
# ===========================================================

def feature_target_split(data):

    X = data.drop("Sales", axis=1)

    y = data["Sales"]

    print("\nFeatures Shape :", X.shape)

    print("Target Shape :", y.shape)

    return X, y


# ===========================================================
# Train Test Split
# ===========================================================

def split_dataset(X, y):

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,

        test_size=0.20,

        random_state=42

    )

    print("\nTraining Samples :", X_train.shape[0])

    print("Testing Samples :", X_test.shape[0])

    return X_train, X_test, y_train, y_test


# ===========================================================
# Complete Preprocessing Pipeline
# ===========================================================

def preprocess_data(file_path):

    # Load Dataset
    data = load_dataset(file_path)

    # Dataset Information
    dataset_information(data)

    # Missing Values
    check_missing_values(data)

    # Remove Duplicate Rows
    data = remove_duplicates(data)

    # Statistical Summary
    statistical_summary(data)

    # Features and Target
    X, y = feature_target_split(data)

    # Split Dataset
    X_train, X_test, y_train, y_test = split_dataset(X, y)

    return (

        data,

        X,

        y,

        X_train,

        X_test,

        y_train,

        y_test

    )