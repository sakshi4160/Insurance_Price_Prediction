import os,sys
from datetime import datetime

# artifact -> pipeline folder ->timestamp -> output

def get_current_timestamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_timestamp()

ROOT_DIR_KEY = os.getcwd()
DATA_DIR = 'Data'
DATA_DIR_KEY = 'insurance.csv'



# artifacts - > data_transformation -> processor /preprocessor.pkl ->and transformation -> train.csv and test.csv

# model training

# model training
MODEL_TRAINER_KEY = 'model_trainer'
MODEL_OBJECT = 'model.pkl'

# batch prediction 


PREDICTION_FOLDER = 'Batch_Prediction'
PREDICTION_CSV = 'Prediction_csv'
PREDICTION_FILE = "output.csv"
TRANFORM_DATA = 'Processed_transformation'