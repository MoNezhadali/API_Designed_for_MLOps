import pandas as pd
from utilities import process_input_data

class ModelInterface:
    """
    Our machine learning algorithm coupled with its pipeline
    """
    def __init__(self, model_path='Requirements/model.pickle', pipeline_path='Requirements/sklearn_pipeline.pickle'):
        with open(model_path, 'rb') as model_file, open(pipeline_path, 'rb') as pipeline_file:
            self.model_version='1.0'
            self.model = pd.read_pickle(model_file)
            self.pipeline = pd.read_pickle(pipeline_file)

    def predict(self, input_data):
        processed_data = pd.DataFrame([process_input_data(input_data)])
        transformed_data = self.pipeline.transform(processed_data)
        prediction = self.model.predict_proba(transformed_data)
        return prediction