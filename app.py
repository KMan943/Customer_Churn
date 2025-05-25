from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler , OneHotEncoder
from xgboost import XGBClassifier

import sys 
import os

from src.pipeline.predict_pipeline import CustomData , PredictPipeline

application = Flask(__name__)

app = application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET' , 'POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data = CustomData(
            Age = float(request.form.get('Age')),
            Tenure = float(request.form.get('Tenure')),
            Usage_Frequency = float(request.form.get('Usage_Frequency')),
            Support_Calls = float(request.form.get('Support_Calls')),
            Payment_Delay = float(request.form.get('Payment_Delay')),
            Total_Spend = float(request.form.get('Total_Spend')),
            Last_Interaction = float(request.form.get('Last_Interaction')),
            Gender = request.form.get('Gender'),
            Subscription_Type = request.form.get('Subscription_Type'),
            Contract_Length = request.form.get('Contract_Length')
        )

        pipeline = PredictPipeline()
        pred = pipeline.predict(data.get_data_as_dataframe())

        return render_template('home.html',predictions = pred[0])
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=5000)