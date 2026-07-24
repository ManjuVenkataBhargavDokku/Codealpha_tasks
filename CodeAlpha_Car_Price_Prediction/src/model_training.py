"""
==============================================================
Project : Car Price Prediction using Machine Learning
Internship : CodeAlpha Data Science Internship
Author : Manju Venkata Bhargav Dokku
==============================================================
"""

import os
import joblib

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

# Create models folder
os.makedirs("../models", exist_ok=True)


def split_dataset(X, y):
    """
    Split dataset into training and testing sets.
    """

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    print("\nDataset Split Successfully")

    print("Training Samples :", len(X_train))
    print("Testing Samples  :", len(X_test))

    return X_train, X_test, y_train, y_test


def train_linear_regression(X_train, y_train):
    """
    Train Linear Regression model.
    """

    print("\nTraining Linear Regression...")

    model = LinearRegression()

    model.fit(X_train, y_train)

    print("Linear Regression Trained Successfully")

    return model


def train_decision_tree(X_train, y_train):
    """
    Train Decision Tree Regressor.
    """

    print("\nTraining Decision Tree Regressor...")

    model = DecisionTreeRegressor(
        random_state=42
    )

    model.fit(X_train, y_train)

    print("Decision Tree Trained Successfully")

    return model


def train_random_forest(X_train, y_train):
    """
    Train Random Forest Regressor.
    """

    print("\nTraining Random Forest Regressor...")

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    print("Random Forest Trained Successfully")

    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluate a regression model.
    """

    predictions = model.predict(X_test)

    r2 = r2_score(y_test, predictions)

    mae = mean_absolute_error(y_test, predictions)

    mse = mean_squared_error(y_test, predictions)

    rmse = mse ** 0.5

    return {
        "R2": r2,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "Predictions": predictions
    }


def compare_models(
        linear_results,
        tree_results,
        forest_results
):
    """
    Compare model performance.
    """

    print("\n")
    print("=" * 60)
    print("MODEL COMPARISON")
    print("=" * 60)

    print("\nLinear Regression")
    print("---------------------")
    print("R² Score :", round(linear_results["R2"], 4))
    print("MAE      :", round(linear_results["MAE"], 4))
    print("RMSE     :", round(linear_results["RMSE"], 4))

    print("\nDecision Tree")
    print("---------------------")
    print("R² Score :", round(tree_results["R2"], 4))
    print("MAE      :", round(tree_results["MAE"], 4))
    print("RMSE     :", round(tree_results["RMSE"], 4))

    print("\nRandom Forest")
    print("---------------------")
    print("R² Score :", round(forest_results["R2"], 4))
    print("MAE      :", round(forest_results["MAE"], 4))
    print("RMSE     :", round(forest_results["RMSE"], 4))

    scores = {
        "Linear Regression": linear_results["R2"],
        "Decision Tree": tree_results["R2"],
        "Random Forest": forest_results["R2"]
    }

    best_model = max(scores, key=scores.get)

    print("\nBest Model :", best_model)

    return best_model


def save_model(model):
    """
    Save trained model.
    """

    model_path = "../models/car_price_model.pkl"

    joblib.dump(model, model_path)

    print("\nModel Saved Successfully")

    print(model_path)