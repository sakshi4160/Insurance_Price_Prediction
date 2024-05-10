
from src.InsurancePricePrediction.logger import logging
from src.InsurancePricePrediction.exception import customexception
import os ,sys
from src.InsurancePricePrediction.utils.utils import load_model
import pandas as pd

class PredictionPipeline():
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            preprocessor_path= os.path.join("artifacts","preprocessor.pkl")
            model_path= os.path.join("artifacts","model.pkl")
            
            preprocessor=load_model(preprocessor_path)
            model=load_model(model_path)
            
            scaled_data=preprocessor.transform(features)
            
            pred=model.predict(scaled_data)
            
            return pred
        
        
        
        except Exception as e:
            logging.info('error occured while processing single prediction')
            customexception(e,sys)
            
    
class CustomData :
    def __init__(self,sex:str,
                    smoker : str,
                    region:str,
                    age:int,
                    bmi:float,
                    children:int
                    ):
        """"categorical_columns = ['sex','smoker','region']
        numerical_columns = ['age','bmi','children']"""
        
        self.sex = sex
        self.smoker = smoker
        self.region = region
        self.age = age
        self.bmi = bmi
        self.children = children
    
    def  get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {'sex':[self.sex],
                                      'smoker':[self.smoker],
                                    'region':[self.region],
                                      'age':[self.age],
                                      'bmi':[self.bmi],
                                      'children':[self.children]
                                      }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        
        
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise customexception(e,sys) 
    
            
            