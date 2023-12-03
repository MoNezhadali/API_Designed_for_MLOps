# Built-in python libraries
import logging
# Side-packages
import pandas as pd
# Internal imports
from utilities import process_input_data

class ModelInterface:
    """
    Our machine learning algorithm coupled with its pipeline
    """
    def __init__(self, model_path='Requirements/model.pickle', pipeline_path='Requirements/sklearn_pipeline.pickle'):
        try:
            self.model_version='1.0'
            with open(model_path, 'rb') as model_file, open(pipeline_path, 'rb') as pipeline_file:
                self.model = pd.read_pickle(model_file)
                self.pipeline = pd.read_pickle(pipeline_file)
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            raise
        except Exception as e:
            logging.error(f"Error initializing ModelInterface: {e}")
            raise

    def predict(self, input_data):
        try:
            processed_data = pd.DataFrame([process_input_data(input_data)])
            transformed_data = self.pipeline.transform(processed_data)
            prediction = self.model.predict_proba(transformed_data)
            return prediction
        except ValueError as e:
            logging.error(f"Value error: {e}")
            if "no_age" or "under_age" in str(e):
                raise ValueError("Either no customer age, minor customer, or invalid request time!") from e    
            else:
                raise
        except Exception as e:
            logging.error(f"Error in prediction: {e}")
            raise