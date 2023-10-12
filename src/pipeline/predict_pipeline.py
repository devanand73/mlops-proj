import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
"""The provided Python code consists of two classes. 

1. `PredictPipeline` is a class that loads a machine learning model and a data preprocessor from specified file paths, applies the preprocessor to input features, and uses the model to make predictions. It handles exceptions using a custom exception class.

2. `CustomData` is a class representing custom data with attributes like gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, reading_score, and writing_score. It provides a method to convert this data into a Pandas DataFrame.

This code is designed for making predictions using a trained machine learning model on custom input data."""

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)


#input data collected from web application and passed on to model for prediction
class CustomData:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score
#collect input custumdata from webpage and convert it as dataframe 
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
