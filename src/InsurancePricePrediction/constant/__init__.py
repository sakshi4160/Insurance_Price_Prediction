import os,sys
from datetime import datetime

# artifact -> pipeline folder ->timestamp -> output

def get_current_timestamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_timestamp()

ROOT_DIR_KEY = os.getcwd()
DATA_DIR = 'Data'
DATA_DIR_KEY = 'insurance.csv'


# batch prediction 

PREDICTION_FOLDER = 'batch_Prediction'
PREDICTION_CSV = 'Prediction_csv'
PREDICTION_FILE = "output.csv"
TRANFORM_DATA = 'Processed_transformation'