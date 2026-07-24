"""
===========================================================
Sales Prediction using Machine Learning
Prediction Module

Author : Manju Venkata Bhargav Dokku
===========================================================
"""

import joblib
import pandas as pd
import os


# ===========================================================
# Save Trained Model
# ===========================================================

def save_model(model):

    os.makedirs("../models", exist_ok=True)

    model_path = "../models/sales_prediction_model.pkl"

    joblib.dump(model, model_path)

    print("\n" + "=" * 60)
    print("MODEL SAVED SUCCESSFULLY")
    print("=" * 60)
    print("Location :", model_path)
    print("=" * 60)


# ===========================================================
# Load Saved Model
# ===========================================================

def load_model():

    model_path = "../models/sales_prediction_model.pkl"

    model = joblib.load(model_path)

    print("\nModel Loaded Successfully.")

    return model


# ===========================================================
# Predict Sales
# ===========================================================

def predict_sales(model):

    print("\n" + "=" * 60)
    print("SAMPLE SALES PREDICTION")
    print("=" * 60)

    # Sample Advertising Budget
    TV = 230.1
    Radio = 37.8
    Newspaper = 69.2

    sample = pd.DataFrame({

        "TV": [TV],
        "Radio": [Radio],
        "Newspaper": [Newspaper]

    })

    prediction = model.predict(sample)

    print("\nAdvertising Budget")

    print(f"TV Advertising         : {TV}")

    print(f"Radio Advertising      : {Radio}")

    print(f"Newspaper Advertising  : {Newspaper}")

    print("\nPredicted Sales")

    print(f"{prediction[0]:.2f} Units")

    print("=" * 60)

    return prediction


# ===========================================================
# Custom Prediction
# ===========================================================

def custom_prediction(model):

    print("\n" + "=" * 60)
    print("CUSTOM SALES PREDICTION")
    print("=" * 60)

    tv = float(input("Enter TV Advertising Budget : "))

    radio = float(input("Enter Radio Advertising Budget : "))

    newspaper = float(input("Enter Newspaper Advertising Budget : "))

    sample = pd.DataFrame({

        "TV": [tv],
        "Radio": [radio],
        "Newspaper": [newspaper]

    })

    prediction = model.predict(sample)

    print("\nPredicted Sales")

    print(f"{prediction[0]:.2f} Units")

    print("=" * 60)