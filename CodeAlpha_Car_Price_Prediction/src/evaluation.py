"""
==============================================================
Project : Car Price Prediction using Machine Learning
Internship : CodeAlpha Data Science Internship
Author : Manju Venkata Bhargav Dokku
==============================================================
"""

import pandas as pd

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)


def evaluate_regression_model(model, X_test, y_test):
    """
    Evaluate Regression Model
    """

    predictions = model.predict(X_test)

    r2 = r2_score(y_test, predictions)

    mae = mean_absolute_error(y_test, predictions)

    mse = mean_squared_error(y_test, predictions)

    rmse = mse ** 0.5

    print("\n")
    print("=" * 70)
    print("MODEL EVALUATION")
    print("=" * 70)

    print(f"R² Score                : {r2:.4f}")
    print(f"Mean Absolute Error     : {mae:.4f}")
    print(f"Mean Squared Error      : {mse:.4f}")
    print(f"Root Mean Squared Error : {rmse:.4f}")

    return predictions


def prediction_report(y_test, predictions):
    """
    Show Actual vs Predicted Values
    """

    report = pd.DataFrame({

        "Actual Price": y_test.values,

        "Predicted Price": predictions

    })

    print("\n")
    print("=" * 70)
    print("ACTUAL VS PREDICTED")
    print("=" * 70)

    print(report.head(15))

    return report


def prediction_error(report):
    """
    Calculate Prediction Error
    """

    report["Difference"] = (

        report["Actual Price"]

        -

        report["Predicted Price"]

    )

    report["Absolute Error"] = (

        report["Difference"].abs()

    )

    print("\n")
    print("=" * 70)
    print("PREDICTION ERROR")
    print("=" * 70)

    print(report.head(15))

    return report


def print_statistics(report):
    """
    Print Error Statistics
    """

    print("\n")
    print("=" * 70)
    print("ERROR STATISTICS")
    print("=" * 70)

    print()

    print("Average Absolute Error :")

    print(

        round(

            report["Absolute Error"].mean(),

            4

        )

    )

    print()

    print("Maximum Error :")

    print(

        round(

            report["Absolute Error"].max(),

            4

        )

    )

    print()

    print("Minimum Error :")

    print(

        round(

            report["Absolute Error"].min(),

            4

        )

    )


def sample_predictions(report):
    """
    Display Sample Predictions
    """

    print("\n")
    print("=" * 70)
    print("SAMPLE PREDICTIONS")
    print("=" * 70)

    for index in range(min(10, len(report))):

        actual = report.iloc[index]["Actual Price"]

        predicted = report.iloc[index]["Predicted Price"]

        print(

            f"Car {index+1}"

        )

        print(

            f"Actual Price    : {actual:.2f} Lakhs"

        )

        print(

            f"Predicted Price : {predicted:.2f} Lakhs"

        )

        print("-" * 50)


def evaluation_summary(model, X_test, y_test):
    """
    Complete Evaluation
    """

    predictions = evaluate_regression_model(

        model,

        X_test,

        y_test

    )

    report = prediction_report(

        y_test,

        predictions

    )

    report = prediction_error(

        report

    )

    print_statistics(

        report

    )

    sample_predictions(

        report

    )

    print("\n")
    print("=" * 70)
    print("MODEL EVALUATION COMPLETED")
    print("=" * 70)

    return predictions