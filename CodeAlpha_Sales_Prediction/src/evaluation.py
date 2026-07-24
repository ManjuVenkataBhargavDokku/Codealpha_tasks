"""
===========================================================
Sales Prediction using Machine Learning
Evaluation Module

Author : Manju Venkata Bhargav Dokku
===========================================================
"""

import numpy as np
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)


# ===========================================================
# Evaluate Model
# ===========================================================

def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    r2 = r2_score(y_test, predictions)

    mae = mean_absolute_error(y_test, predictions)

    mse = mean_squared_error(y_test, predictions)

    rmse = np.sqrt(mse)

    print("\n" + "=" * 60)
    print("MODEL EVALUATION")
    print("=" * 60)

    print(f"R² Score                 : {r2:.4f}")

    print(f"Mean Absolute Error      : {mae:.4f}")

    print(f"Mean Squared Error       : {mse:.4f}")

    print(f"Root Mean Squared Error  : {rmse:.4f}")

    print("=" * 60)

    return predictions


# ===========================================================
# Print Evaluation Summary
# ===========================================================

def evaluation_summary(best_model_name):

    print("\n" + "=" * 60)
    print("BEST MODEL SUMMARY")
    print("=" * 60)

    print(f"Selected Model : {best_model_name}")

    print("\nEvaluation completed successfully.")

    print("=" * 60)