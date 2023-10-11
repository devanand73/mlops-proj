# Import necessary modules and libraries
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

"""This Python code defines a Flask web application that serves a predictive model. It imports necessary modules, creates a Flask app, and defines two routes:

1. The root route `'/'` renders an 'index.html' template for the home page.
2. The '/predictdata' route handles both GET and POST requests, collecting data from a web form, processing it, and making predictions using a predictive pipeline. The predictions are then displayed on the web page.

The script also includes a block to run the Flask application when executed directly, listening on host "0.0.0.0"."""

# Create a Flask application
application = Flask(__name__)
app = application  # Alias the application object as 'app'

# Define a route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for predicting data points
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # Collect data from a web form and create a DataFrame
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        # Use a predictive pipeline to make predictions
        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)
        print("After Prediction")

        # Return the prediction results to the web page
        return render_template('home.html', results=results[0])

# Run the Flask application if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0")
