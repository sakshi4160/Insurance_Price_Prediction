from src.InsurancePricePrediction.components.data_ingestion import DataIngestion

from src.InsurancePricePrediction.components.data_transformation import DataTransformation

from src.InsurancePricePrediction.components.model_trainer import ModelTrainer


import os
import sys
from src.InsurancePricePrediction.logger import logging
from src.InsurancePricePrediction.exception import customexception
import pandas as pd


class Train:
    def __init__(self):
        self.c = 0
        print(f"************************************{self.c}**************************************")
    
    def main(self):
        
        obj = DataIngestion()
        train_data,test_data = obj.initiate_data_ingestion()
        data_transformation = DataTransformation()
        train_arr,test_arr,_ = data_transformation.initialize_data_transformation(train_data,test_data)
        model_trainer = ModelTrainer()
        print(model_trainer.initate_model_training(train_arr,test_arr))