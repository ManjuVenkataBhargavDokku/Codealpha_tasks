"""
===========================================================
Sales Prediction using Machine Learning
Model Training Module

Author : Manju Venkata Bhargav Dokku
===========================================================
"""

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

import numpy as np


# ===========================================================
# Evaluate Model
# ===========================================================

def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    r2 = r2_score(y_test, predictions)

    mae = mean_absolute_error(y_test, predictions)

    mse = mean_squared_error(y_test, predictions)

    rmse = np.sqrt(mse)

    return {

        "R2": r2,

        "MAE": mae,

        "MSE": mse,

        "RMSE": rmse,

        "Predictions": predictions

    }


# ===========================================================
# Train Linear Regression
# ===========================================================

def train_linear_regression(X_train, X_test, y_train, y_test):

    print("\nTraining Linear Regression Model...")

    model = LinearRegression()

    model.fit(X_train, y_train)

    results = evaluate_model(model, X_test, y_test)

    print("Linear Regression Completed")

    return model, results


# ===========================================================
# Train Decision Tree
# ===========================================================

def train_decision_tree(X_train, X_test, y_train, y_test):

    print("\nTraining Decision Tree Regressor...")

    model = DecisionTreeRegressor(

        random_state=42

    )

    model.fit(X_train, y_train)

    results = evaluate_model(model, X_test, y_test)

    print("Decision Tree Completed")

    return model, results


# ===========================================================
# Train Random Forest
# ===========================================================

def train_random_forest(X_train, X_test, y_train, y_test):

    print("\nTraining Random Forest Regressor...")

    model = RandomForestRegressor(

        n_estimators=200,

        random_state=42

    )

    model.fit(X_train, y_train)

    results = evaluate_model(model, X_test, y_test)

    print("Random Forest Completed")

    return model, results


# ===========================================================
# Compare Models
# ===========================================================

def compare_models(linear_results,
                   decision_results,
                   random_results):

    print("\n" + "=" * 65)

    print("MODEL COMPARISON")

    print("=" * 65)

    print("{:<22} {:>10}".format("Model", "R² Score"))

    print("-" * 65)

    print("{:<22} {:>10.4f}".format(

        "Linear Regression",

        linear_results["R2"]

    ))

    print("{:<22} {:>10.4f}".format(

        "Decision Tree",

        decision_results["R2"]

    ))

    print("{:<22} {:>10.4f}".format(

        "Random Forest",

        random_results["R2"]

    ))

    print("=" * 65)


# ===========================================================
# Select Best Model
# ===========================================================

def best_model(

    linear_model,
    decision_model,
    random_model,

    linear_results,
    decision_results,
    random_results

):

    scores = {

        "Linear Regression": linear_results["R2"],

        "Decision Tree": decision_results["R2"],

        "Random Forest": random_results["R2"]

    }

    best = max(scores, key=scores.get)

    print("\nBest Model :", best)

    if best == "Linear Regression":

        return linear_model, linear_results, best

    elif best == "Decision Tree":

        return decision_model, decision_results, best

    else:

        return random_model, random_results, best


# ===========================================================
# Train All Models
# ===========================================================

def train_models(

    X_train,

    X_test,

    y_train,

    y_test

):

    linear_model, linear_results = train_linear_regression(

        X_train,

        X_test,

        y_train,

        y_test

    )

    decision_model, decision_results = train_decision_tree(

        X_train,

        X_test,

        y_train,

        y_test

    )

    random_model, random_results = train_random_forest(

        X_train,

        X_test,

        y_train,

        y_test

    )

    compare_models(

        linear_results,

        decision_results,

        random_results

    )

    model, results, name = best_model(

        linear_model,

        decision_model,

        random_model,

        linear_results,

        decision_results,

        random_results

    )

    return model, results, name