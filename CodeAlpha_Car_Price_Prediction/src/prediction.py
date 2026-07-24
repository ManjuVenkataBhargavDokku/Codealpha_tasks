"""
==============================================================
Project : Car Price Prediction using Machine Learning
Internship : CodeAlpha Data Science Internship
Author : Manju Venkata Bhargav Dokku
==============================================================
"""

import joblib
import pandas as pd


def load_saved_model():
    """
    Load trained Random Forest model.
    """

    model_path = "../models/car_price_model.pkl"

    model = joblib.load(model_path)

    print("\nModel Loaded Successfully")

    return model


def predict_price(model, input_data):
    """
    Predict car selling price.
    """

    prediction = model.predict(input_data)

    return prediction[0]


def sample_prediction(model):
    """
    Predict the price of a sample car.
    """

    print("\n")
    print("=" * 70)
    print("SAMPLE CAR PRICE PREDICTION")
    print("=" * 70)

    # Change these values according to your dataset
    sample = pd.DataFrame({

        "Car_Name": [90],

        "Present_Price": [8.50],

        "Driven_kms": [35000],

        "Fuel_Type": [1],

        "Selling_type": [0],

        "Transmission": [1],

        "Owner": [0],

        "Car_Age": [6]

    })

    predicted_price = predict_price(
        model,
        sample
    )

    print("\nSample Car Details")

    print(sample)

    print("\nPredicted Selling Price")

    print(f"₹ {predicted_price:.2f} Lakhs")

    return predicted_price


def custom_prediction(model):
    """
    Predict using user input.
    """

    print("\n")
    print("=" * 70)
    print("CUSTOM CAR PRICE PREDICTION")
    print("=" * 70)

    car_name = int(input("Encoded Car Name : "))

    present_price = float(input("Present Price : "))

    driven_kms = int(input("Driven Kilometers : "))

    fuel_type = int(input("Fuel Type (Encoded) : "))

    selling_type = int(input("Selling Type (Encoded) : "))

    transmission = int(input("Transmission (Encoded) : "))

    owner = int(input("Owner : "))

    car_age = int(input("Car Age : "))

    user_data = pd.DataFrame({

        "Car_Name": [car_name],

        "Present_Price": [present_price],

        "Driven_kms": [driven_kms],

        "Fuel_Type": [fuel_type],

        "Selling_type": [selling_type],

        "Transmission": [transmission],

        "Owner": [owner],

        "Car_Age": [car_age]

    })

    prediction = predict_price(
        model,
        user_data
    )

    print("\nPredicted Selling Price")

    print(f"₹ {prediction:.2f} Lakhs")

    return prediction


def prediction_summary():
    """
    Display project completion message.
    """

    print("\n")
    print("=" * 70)
    print("CAR PRICE PREDICTION COMPLETED SUCCESSFULLY")
    print("=" * 70)

    print("\nThe trained model can now predict")
    print("the selling price of any used car.")

    print("\nModel Location")

    print("../models/car_price_model.pkl")