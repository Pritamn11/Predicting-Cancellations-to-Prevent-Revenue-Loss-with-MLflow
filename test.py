from src.utils.common import *
from pathlib import Path    
from src.utils.exception import CustomException
from src.utils.logger import logging
import sys
import pandas as pd
from src.pipeline.predict_pipeline import PredictionPipeline, CustomData





data = CustomData(number_of_adults=1,number_of_children=1,number_of_weekend_nights=2,
                number_of_week_nights=5, type_of_meal='Meal Plan 1', car_parking_space=0,
                room_type='Room_Type 1', lead_time=224,market_segment_type='Offline',
                repeated=0, P_C=0, P_not_C=0, average_price= 88, special_requests=0,month=10)


input_df = data.get_data_as_frame()


obj = PredictionPipeline()


transform_data = obj.preprocessing(input_df)
result = obj.predict(data=transform_data)
a = int(result[0]) 
print(a)
