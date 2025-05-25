import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from exception import CustomExeption
from logger import logging
from utils import load_object

from src.components.data_ingestion import DataIngestion , DataIngestionConfig
from src.components.data_transformation import DataTransformation , DataTransformationConfig

import pandas as pd
import numpy as np

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self , features):
        try:
            model_path = 'models/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)

            pred = model.predict(data_scaled)

            return pred
        except Exception as e:
            logging.info('failed to predict the output')
            raise CustomExeption(e,sys)



class CustomData:
    def __init__(self,
                Age:int, Tenure:int, Usage_Frequency:int, Support_Calls:int,
                Payment_Delay:int, Total_Spend:int, Last_Interaction:int,
                Gender:str, Subscription_Type:str, Contract_Length:str):
        self.Age = Age
        self.Tenure = Tenure
        self.Usage_Frequency = Usage_Frequency
        self.Support_Calls = Support_Calls
        self.Payment_Delay = Payment_Delay
        self.Total_Spend = Total_Spend
        self.Last_Interaction = Last_Interaction
        self.Gender = Gender
        self.Subscription_Type = Subscription_Type
        self.Contract_Length = Contract_Length

    def get_data_as_dataframe(self):
        try:
            data = {
                # Age,Gender,Tenure,Usage Frequency,Support Calls,Payment Delay,Subscription Type,Contract Length,Total Spend,Last Interaction
                "Age" : [self.Age],
                "Gender" : [self.Gender],
                "Tenure" : [self.Tenure],
                "Usage Frequency" : [self.Usage_Frequency],
                "Support Calls" : [self.Support_Calls],
                "Payment Delay" : [self.Payment_Delay],
                "Subscription Type" : [self.Subscription_Type],
                "Contract Length" : [self.Contract_Length],
                "Total Spend" : [self.Total_Spend],
                "Last Interaction" : [self.Last_Interaction]
            }

            df = pd.DataFrame(data)
            return df
        except Exception as e:
            logging.info("Falied to convert data to dataframe")
            raise CustomExeption(e,sys)
           
        

