import pickle
from src.InsurancePricePrediction.logger import logging
from src.InsurancePricePrediction.exception import customexception
import os,sys
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_obj(filepath,obj):
    try:
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path,exist_ok=True)
        
        with open(filepath,'wb') as file_obj:
            pickle.dump(obj,file_obj)
        
    except Exception as e:
        customexception(e,sys)
        
        
def evaluate_model(X_train, y_train,X_test, y_test, models):
    try:
        report = {}

        for i in range(len(models)):
            model = list(models.values())[i]

            model.fit(X_train, y_train)

            y_test_pred = model.predict(X_test)

            test_model_score = r2_score(y_test,y_test_pred )

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        logging.info('Exception occured while evaluating model')
        raise customexception(e,sys)   
    

def load_model(filepath):
    try:
        with open(filepath,'rb') as f:
            return pickle.load(f)
    
    except Exception as e:
        
        logging.info('Exception occured while loading model')
        customexception(e,sys)