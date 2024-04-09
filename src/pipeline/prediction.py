import joblib 
import pandas as pd 
import numpy as np 
from pathlib import Path 


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))
        self.preprocessor = joblib.load("artifacts/data_transformation/preprocessor.joblib")
    
    def preprocessing(self, data):
        preprocessing_data = self.preprocessor.transform(data)
        return preprocessing_data

    def predict(self, data):
        prediction = self.model.predict(data)
        return prediction
    



if __name__=="__main__":
    obj = PredictionPipeline()
    input_data = {
    'number of adults': [1],
    'number of children': [1],
    'number of weekend nights': [2],
    'number of week nights': [5],
    'type of meal': ['Meal Plan 1'],
    'car parking space': [0],
    'room type': ['Room_Type 1'],
    'lead time': [224],
    'market segment type': ['Offline'],
    'repeated': [0],
    'P-C': [0],
    'P-not-C': [0],
    'average price': [88.0],
    'special requests': [0],
    'month': [10]
}


    input_df = pd.DataFrame(input_data)
    
    transform_data = obj.preprocessing(input_df)
    print(obj.predict(data=transform_data))