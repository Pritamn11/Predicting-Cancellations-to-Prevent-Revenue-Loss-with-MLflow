from flask import Flask, render_template, request 
import os 
import numpy as np
import pandas as pd
from src.pipeline.prediction import PredictionPipeline 



app = Flask(__name__)


@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/train',methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Succcessfull"

@app.route('/predict',methods=['GET'])
def predict():
    if request.method == 'POST':
        try:
            # number_of_adults: int64
            # number_of_children: int64
            # number_of_weekend nights: int64
            # number_of_week nights: int64
            # type_of_meal: object
            # car_parking_space: int64
            # room_type: object
            # lead_time: int64
            # market_segment_type: object
            # repeated: int64
            # P_C: int64
            # P_not_C: int64
            # average_price: float64
            # special_requests: int64
            # month 
            pass
     
        except Exception as e:
            print("the exception message is :",e)
            return "Error occured"

    return render_template('result.html')





if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)