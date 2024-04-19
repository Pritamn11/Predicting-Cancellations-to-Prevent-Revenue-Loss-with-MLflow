from flask import Flask, render_template, request 
import os 
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import PredictionPipeline, CustomData



app = Flask(__name__)


@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/train',methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Succcessfull"


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'GET':
        return render_template("result.html")
    else:

        data = CustomData(
            number_of_adults = int(request.form['number_of_adults']),
            number_of_children = int(request.form['number_of_children']),
            number_of_weekend_nights = int(request.form['number_of_weekend_nights']),
            number_of_week_nights = int(request.form['number_of_week_nights']),
            type_of_meal = request.form['type_of_meal'],
            car_parking_space = int(request.form['car_parking_space']),
            room_type = request.form['room_type'],
            lead_time = int(request.form['lead_time']),
            market_segment_type = request.form['market_segment_type'],
            repeated = int(request.form['repeated']),
            P_C = int(request.form['P_C']),
            P_not_C = int(request.form['P_not_C']),
            average_price = float(request.form['average_price']),
            special_requests = int(request.form['special_requests']),
            month = int(request.form['month'])
                )
                
        input_df = data.get_data_as_frame()
        
        
        obj = PredictionPipeline()
        transform_data = obj.preprocessing(input_df)
        result = obj.predict(data=transform_data)
        
        return render_template("result.html", output = int(result[0]))
    
    
        










if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)