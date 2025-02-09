# -*- coding: utf-8 -*-

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Define the hyperparameter grid
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

# Create a Random Forest Classifier
rf = RandomForestClassifier()

# Create GridSearchCV object
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring='accuracy')

# Fit the model to the data
grid_search.fit(X, y)

# Print the best hyperparameters
print("Best hyperparameters:", grid_search.best_params_)

# ... (previous code from the last response) ...

# Print the best hyperparameters
print("Best hyperparameters:", grid_search.best_params_)

# Print the best cross-validated accuracy score
print("Best cross-validated accuracy score:", grid_search.best_score_)

pip install mlflow

import mlflow

mlflow.set_experiment(experiment_name="RandomForest_Hyperparameter_Tuning")

!mlflow ui

import mlflow
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV

# Set the MLflow experiment
mlflow.set_experiment(experiment_name="RandomForest_Hyperparameter_Tuning")

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Define the hyperparameter grid
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

# Create a Random Forest Classifier
rf = RandomForestClassifier()

# Create GridSearchCV object
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring='accuracy')

# Start an MLflow run
with mlflow.start_run():
    # Fit the model to the data
    grid_search.fit(X, y)

    # Log the best hyperparameters
    mlflow.log_params(grid_search.best_params_)

    # Log the best cross-validated accuracy score
    mlflow.log_metric("accuracy", grid_search.best_score_)

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Enable MLflow autologging
mlflow.autolog()

# Load the dataset
data = pd.read_csv(r"iris_dataset.csv")
data.head()

# Create feature space and target
X = data[["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]]
y = data["target"]
print(X, y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define the parameter grid
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

# Create a RandomForestClassifier object
rf = RandomForestClassifier()

# Create a GridSearchCV object
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5)

# Start MLflow run
from mlflow import log_metric, log_param, log_artifacts
with mlflow.start_run():
    # Fit the GridSearchCV object to the data
    grid_search.fit(X_train, y_train)

    # Log the best parameters and score
    mlflow.log_params(grid_search.best_params_)
    mlflow.log_metric("best_score", grid_search.best_score_)

    # Log the model
    mlflow.sklearn.log_model(grid_search.best_estimator_, "model")

    # Print the best parameters and the best score
    print("Best Parameters:", grid_search.best_params_)
    print("Best Score:", grid_search.best_score_)
