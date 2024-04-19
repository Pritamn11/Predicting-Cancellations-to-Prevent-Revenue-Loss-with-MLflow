import joblib 
import pandas as pd 
import numpy as np 
from pathlib import Path 
from src.utils.exception import CustomException
import sys


class PredictionPipeline:
    try :
        def __init__(self):
            self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))
            self.preprocessor = joblib.load("artifacts/data_transformation/preprocessor.joblib")
        
        def preprocessing(self, data):
            preprocessing_data = self.preprocessor.transform(data)
            return preprocessing_data

        def predict(self, data):
            prediction = self.model.predict(data)
            return prediction
    
    except Exception as e:
        raise CustomException(e,sys)



class CustomData:
    def __init__(self, number_of_adults:int,
                    number_of_children:int, 
                    number_of_weekend_nights:int,
                    number_of_week_nights:int,
                    type_of_meal:str,
                    car_parking_space:int,
                    room_type:str,
                    lead_time:int,
                    market_segment_type:str,
                    repeated : int,
                    P_C : int,
                    P_not_C : int,
                    average_price :float,
                    special_requests : int,
                    month : int):
            
        self.number_of_adults = number_of_adults
        self.number_of_children = number_of_children
        self.number_of_weekend_nights = number_of_weekend_nights
        self.number_of_week_nights = number_of_week_nights
        self.type_of_meal = type_of_meal
        self.car_parking_space = car_parking_space
        self.room_type = room_type
        self.lead_time = lead_time
        self.market_segment_type = market_segment_type
        self.repeated = repeated
        self.P_C = P_C
        self.P_not_C = P_not_C
        self.average_price = average_price
        self.special_requests = special_requests
        self.month = month
        

    def get_data_as_frame(self):
        try:
            custom_data_input_dict = {
                "number of adults": [self.number_of_adults],
                "number of children": [self.number_of_children],
                "number of weekend nights": [self.number_of_weekend_nights],
                "number of week nights": [self.number_of_week_nights],
                "type of meal": [self.type_of_meal],
                "car parking space": [self.car_parking_space],
                "room type": [self.room_type],
                "lead time": [self.lead_time],
                "market segment type": [self.market_segment_type],
                "repeated": [self.repeated],
                "P-C": [self.P_C],
                "P-not-C": [self.P_not_C],
                "average price": [self.average_price],
                "special requests": [self.special_requests],
                "month": [self.month]
                
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e,sys)   








# if __name__=="__main__":
#     obj = PredictionPipeline()
#     input_data = {
#     'number of adults': [1],
#     'number of children': [1],
#     'number of weekend nights': [2],
#     'number of week nights': [5],
#     'type of meal': ['Meal Plan 1'],
#     'car parking space': [0],
#     'room type': ['Room_Type 1'],
#     'lead time': [224],
#     'market segment type': ['Offline'],
#     'repeated': [0],
#     'P-C': [0],
#     'P-not-C': [0],
#     'average price': [88.0],
#     'special requests': [0],
#     'month': [10]
# }


#     input_df = pd.DataFrame(input_data)
    
#     transform_data = obj.preprocessing(input_df)
#     result = obj.predict(data=transform_data)
#     a = int(result[0]) 
#     print(a)
