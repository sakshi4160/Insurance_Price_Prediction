from src.InsurancePricePrediction.constant import *
import os,sys

ROOT_DIR = ROOT_DIR_KEY


# batch prediction 

TRANFORM_PROCESSED = os.path.join(ROOT_DIR,PREDICTION_FOLDER,TRANFORM_DATA)
BATCH_PREDICTION=os.path.join(ROOT_DIR,PREDICTION_FOLDER,PREDICTION_CSV,PREDICTION_FILE)