
from src.InsurancePricePrediction.logger import logging
from src.InsurancePricePrediction.exception import customexception
import os,sys

from src.InsurancePricePrediction.components.data_transformation import DataTransformation,DataTransformationConfig
from src.InsurancePricePrediction.components.model_trainer import ModelTrainer
from src.InsurancePricePrediction.components.data_ingestion import DataIngestion
from flask import Flask, request,render_template,jsonify

from src.InsurancePricePrediction.pipelines.prediction_pipeline import CustomData, PredictionPipeline
from batch.batch import BatchPrediction


transformer_file_path = os.path.join('artifacts','preprocessor.pkl')
model_file_path = os.path.join('artifacts','model.pkl')


application = Flask(__name__, template_folder="templates")
app = application


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")

    else:
        data = CustomData(
            age = int(request.form.get('age')),
            sex=  request.form.get('sex'),
            smoker=  request.form.get('smoker'),
            children = int(request.form.get('children')),
            bmi=  float(request.form.get('bmi')),
            region=  request.form.get('region'),
           
            
        )
        
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictionPipeline()
        pred = predict_pipeline.predict(final_new_data)
        
        result = int(pred[0])
        
        return render_template('form.html',final_result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port ='8888',debug=True)