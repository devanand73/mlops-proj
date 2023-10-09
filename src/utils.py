# Import necessary libraries
import os
import sys
import numpy as np
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
''' The provided code defines three functions: `save_object`, `evaluate_models`, and `load_object`. 

1. `save_object` saves a Python object to a specified file path using pickle after creating necessary directories, handling exceptions, and raising a custom exception if an error occurs.

2. `evaluate_models` performs machine learning model evaluation and hyperparameter tuning using GridSearchCV. It calculates R-squared scores for multiple models on both training and testing data, returning a dictionary with the testing R-squared scores.

3. `load_object` loads a Python object from a file using pickle and returns it, handling exceptions and raising a custom exception if an error occurs.

These functions are designed for machine learning model management, including saving and loading models and evaluating their performance.'''

# Import CustomException from a custom module named 'src.exception'
from src.exception import CustomException

# Define a function to save an object to a file
def save_object(file_path, obj):
    try:
        # Get the directory path from the file path
        dir_path = os.path.dirname(file_path)

        # Create the directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)

        # Open the file in binary write mode and dump the object using pickle
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        # Raise a CustomException with the error and sys information
        raise CustomException(e, sys)

# Define a function to evaluate machine learning models
def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        # Create an empty dictionary to store evaluation results
        report = {}

        # Iterate through models and their corresponding hyperparameters
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            # Use GridSearchCV to perform hyperparameter tuning
            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            # Set the model's parameters to the best hyperparameters and retrain
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # Make predictions on the training and testing data
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # Calculate the R-squared (R2) score for both training and testing data
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            # Store the testing R2 score in the report dictionary
            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        # Raise a CustomException with the error and sys information
        raise CustomException(e, sys)

# Define a function to load an object from a file
def load_object(file_path):
    try:
        # Open the file in binary read mode and load the object using pickle
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        # Raise a CustomException with the error and sys information
        raise CustomException(e, sys)
