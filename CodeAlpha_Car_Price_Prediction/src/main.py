"""
==============================================================
Project : Car Price Prediction using Machine Learning
Internship : CodeAlpha Data Science Internship
Author : Manju Venkata Bhargav Dokku
==============================================================
"""

from data_preprocessing import (
    load_dataset,
    dataset_information,
    clean_dataset,
    split_features_target
)

from visualization import (
    dataset_preview,
    price_distribution,
    box_plot,
    correlation_heatmap,
    brand_analysis,
    fuel_type_distribution,
    transmission_distribution,
    owner_distribution,
    car_age_distribution,
    feature_importance,
    actual_vs_predicted,
    residual_plot,
    project_completed
)

from model_training import (
    split_dataset,
    train_linear_regression,
    train_decision_tree,
    train_random_forest,
    evaluate_model,
    compare_models,
    save_model
)

from evaluation import (
    evaluation_summary
)

from prediction import (
    load_saved_model,
    sample_prediction,
    prediction_summary
)


def main():

    print("=" * 70)
    print("CAR PRICE PREDICTION USING MACHINE LEARNING")
    print("CodeAlpha Data Science Internship")
    print("Developed by Manju Venkata Bhargav Dokku")
    print("=" * 70)

    # ---------------------------------------------------
    # Load Dataset
    # ---------------------------------------------------

    file_path = "../dataset/car data.csv"

    data = load_dataset(file_path)

    # ---------------------------------------------------
    # Dataset Information
    # ---------------------------------------------------

    dataset_information(data)

    # ---------------------------------------------------
    # Data Cleaning
    # ---------------------------------------------------

    data = clean_dataset(data)

    # ---------------------------------------------------
    # Save Dataset Preview
    # ---------------------------------------------------

    dataset_preview(data)

    # ---------------------------------------------------
    # Generate Visualizations
    # ---------------------------------------------------

    print("\nGenerating Visualizations...\n")

    price_distribution(data)

    box_plot(data)

    correlation_heatmap(data)

    brand_analysis(data)

    fuel_type_distribution(data)

    transmission_distribution(data)

    owner_distribution(data)

    car_age_distribution(data)

    # ---------------------------------------------------
    # Features & Target
    # ---------------------------------------------------

    X, y = split_features_target(data)

    # ---------------------------------------------------
    # Train Test Split
    # ---------------------------------------------------

    X_train, X_test, y_train, y_test = split_dataset(
        X,
        y
    )

    # ---------------------------------------------------
    # Train Models
    # ---------------------------------------------------

    linear_model = train_linear_regression(
        X_train,
        y_train
    )

    tree_model = train_decision_tree(
        X_train,
        y_train
    )

    forest_model = train_random_forest(
        X_train,
        y_train
    )

    # ---------------------------------------------------
    # Evaluate Models
    # ---------------------------------------------------

    linear_results = evaluate_model(
        linear_model,
        X_test,
        y_test
    )

    tree_results = evaluate_model(
        tree_model,
        X_test,
        y_test
    )

    forest_results = evaluate_model(
        forest_model,
        X_test,
        y_test
    )

    # ---------------------------------------------------
    # Compare Models
    # ---------------------------------------------------

    best_model = compare_models(
        linear_results,
        tree_results,
        forest_results
    )

    # ---------------------------------------------------
    # Select Best Model
    # ---------------------------------------------------

    if best_model == "Linear Regression":
        final_model = linear_model
        predictions = linear_results["Predictions"]

    elif best_model == "Decision Tree":
        final_model = tree_model
        predictions = tree_results["Predictions"]

    else:
        final_model = forest_model
        predictions = forest_results["Predictions"]

    # ---------------------------------------------------
    # Detailed Evaluation
    # ---------------------------------------------------

    evaluation_summary(
        final_model,
        X_test,
        y_test
    )

    # ---------------------------------------------------
    # Prediction Graphs
    # ---------------------------------------------------

    actual_vs_predicted(
        y_test,
        predictions
    )

    residual_plot(
        y_test,
        predictions
    )

    # ---------------------------------------------------
    # Save Model
    # ---------------------------------------------------

    save_model(final_model)

    # ---------------------------------------------------
    # Load Saved Model
    # ---------------------------------------------------

    model = load_saved_model()

    # ---------------------------------------------------
    # Sample Prediction
    # ---------------------------------------------------

    sample_prediction(model)

    prediction_summary()

    project_completed()

    print("\n")
    print("=" * 70)
    print("PROJECT COMPLETED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    main()