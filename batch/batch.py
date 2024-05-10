
import os,sys
import pandas as pd
import numpy as np
from src.InsurancePricePrediction.logger import logging
from src.InsurancePricePrediction.exception import customexception
import joblib
from src.InsurancePricePrediction.utils.utils import load_model
from sklearn.pipeline import Pipeline
from src.InsurancePricePrediction.constant import *
from src.InsurancePricePrediction.config.configuration import *



class BatchPrediction(object):
    def __init__(self,input_file,
                 model_file_path,
                 transformer_file_path,)->None:
        
        self.input_file = input_file
        self.model_file_path = model_file_path
        self.transformer_file_path = transformer_file_path
        
    
    def start_batch_prediction(self):
        try:
            # load the data transformation pipeline file path
            with open(self.transformer_file_path,'rb') as f:
                processed = joblib.load(f)
                
            # load the model sepratly
            model = load_model(file_path=self.model_file_path)
            
            # loading the csv
            
            df = pd.read_csv(self.input_file)
            
            # Data transformation 
            transformed_data = processed.transform(df)
            
            file_path = os.path.join(TRANFORM_PROCESSED,"processed.csv")
            prediction = model.predict(transformed_data) 
            
            df_prediction = pd.DataFrame(prediction,columns=['prediction'])
            
              # Save the predictions to a CSV file
            batch_prediction_path = os.path.join(BATCH_PREDICTION)
            os.makedirs(os.path.dirname(batch_prediction_path), exist_ok=True)
            df_prediction.to_csv(batch_prediction_path, index=False)
            logging.info(f"Batch predictions saved to '{batch_prediction_path}'.")
            
            
            logging.info("Batch Prediction successfully completed")
                       
                       
        
        except Exception as e:
            logging.info("Exception occurred in Batch Prediction")
            customexception(e,sys)