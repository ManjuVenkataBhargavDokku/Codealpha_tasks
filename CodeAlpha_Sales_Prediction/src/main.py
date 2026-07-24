"""
===========================================================
Sales Prediction using Machine Learning

Main Program

Author : Manju Venkata Bhargav Dokku
===========================================================
"""

import os

from data_preprocessing import preprocess_data

from visualization import (
    generate_visualizations,
    feature_importance,
    actual_vs_predicted,
    residual_plot
)

from model_training import train_models

from evaluation import (
    evaluate_model,
    evaluation_summary
)

from prediction import (
    save_model,
    predict_sales,
    custom_prediction
)


# ===========================================================
# Main Function
# ===========================================================

def main():

    print("=" * 70)
    print(" SALES PREDICTION USING MACHINE LEARNING ")
    print("=" * 70)

    # -------------------------------------------------------
    # Dataset Path
    # -------------------------------------------------------

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    dataset_path = os.path.join(
        BASE_DIR,
        "..",
        "dataset",
        "Advertising.csv"
    )

    # -------------------------------------------------------
    # Data Preprocessing
    # -------------------------------------------------------

    (
        data,
        X,
        y,
        X_train,
        X_test,
        y_train,
        y_test
    ) = preprocess_data(dataset_path)

    # -------------------------------------------------------
    # Data Visualization
    # -------------------------------------------------------

    print("\nGenerating Visualizations...")

    generate_visualizations(data)

    print("Visualizations Generated Successfully.")

    # -------------------------------------------------------
    # Model Training
    # -------------------------------------------------------

    print("\nTraining Machine Learning Models...")

    best_model, results, best_model_name = train_models(

        X_train,
        X_test,
        y_train,
        y_test

    )

    # -------------------------------------------------------
    # Model Evaluation
    # -------------------------------------------------------

    predictions = evaluate_model(

        best_model,

        X_test,

        y_test

    )

    evaluation_summary(best_model_name)

    # -------------------------------------------------------
    # Prediction Graphs
    # -------------------------------------------------------

    actual_vs_predicted(

        y_test,

        predictions

    )

    residual_plot(

        y_test,

        predictions

    )

    # -------------------------------------------------------
    # Feature Importance
    # -------------------------------------------------------

    if hasattr(best_model, "feature_importances_"):

        feature_importance(

            best_model,

            X.columns

        )

        print("\nFeature Importance Graph Saved.")

    else:

        print("\nFeature Importance not available for this model.")

    # -------------------------------------------------------
    # Save Model
    # -------------------------------------------------------

    save_model(best_model)

    # -------------------------------------------------------
    # Sample Prediction
    # -------------------------------------------------------

    predict_sales(best_model)

    # -------------------------------------------------------
    # Custom Prediction (Optional)
    # -------------------------------------------------------

    choice = input("\nDo you want to predict custom sales? (yes/no): ")

    if choice.lower() == "yes":

        custom_prediction(best_model)

    # -------------------------------------------------------
    # Completion Message
    # -------------------------------------------------------

    print("\n" + "=" * 70)

    print("PROJECT COMPLETED SUCCESSFULLY")

    print("=" * 70)

    print("Images saved inside      : images/")

    print("Model saved inside       : models/")

    print("Notebook folder          : notebooks/")

    print("Source Code              : src/")

    print("=" * 70)

    print("\nThank you for using the Sales Prediction Project!")

    print("\nDeveloped By")

    print("Manju Venkata Bhargav Dokku")

    print("=" * 70)


# ===========================================================
# Run Program
# ===========================================================

if __name__ == "__main__":

    main()