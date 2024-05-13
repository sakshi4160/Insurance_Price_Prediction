
from src.InsurancePricePrediction.logger import logging
from src.InsurancePricePrediction.exception import customexception
import os,sys

from src.InsurancePricePrediction.components.data_transformation import DataTransformation,DataTransformationConfig
from src.InsurancePricePrediction.components.model_trainer import ModelTrainer
from src.InsurancePricePrediction.components.data_ingestion import DataIngestion
from flask import Flask, request,render_template,jsonify
from src.InsurancePricePrediction.pipelines.training_pipeline import Train

from src.InsurancePricePrediction.pipelines.prediction_pipeline import CustomData, PredictionPipeline
from batch.batch import BatchPrediction
from werkzeug.utils import secure_filename


transformer_file_path = os.path.join('artifacts','preprocessor.pkl')
model_file_path = os.path.join('artifacts','model.pkl')

UPLOAD_FOLDER = "batch_Prediction/UPLOAD_CSV_FILE"

application = Flask(__name__, template_folder="templates")
app = application

ALLOWED_EXTENSION = {'csv'}


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


@app.route("/batch", methods=['GET','POST'])
def perform_batch_prediction():
    
    
    if request.method == 'GET':
        return render_template('batch.html')
    else:
        file = request.files['csv_file']  # Update the key to 'csv_file'
        # Directory path
        directory_path = UPLOAD_FOLDER
        # Create the directory
        os.makedirs(directory_path, exist_ok=True)

        # Check if the file has a valid extension
        if file and '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION:
            # Delete all files in the file path
            for filename in os.listdir(os.path.join(UPLOAD_FOLDER)):
                file_path = os.path.join(UPLOAD_FOLDER, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)

            # Save the new file to the uploads directory
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            print(file_path)

            logging.info("CSV received and Uploaded")

            # Perform batch prediction using the uploaded file
            batch = BatchPrediction(file_path,
                                    model_file_path,
                                    transformer_file_path,
                                    )
            batch.start_batch_prediction()

            output = "Batch Prediction Done"
            return render_template("batch.html", prediction_result=output, prediction_type='batch')
        else:
            return render_template('batch.html', prediction_type='batch', error='Invalid file type')
        

@app.route('/train', methods=['GET', 'POST'])
def train():
    if request.method == 'GET':
        return render_template('train.html')
    else:
        try:
            pipeline = Train()
            pipeline.main()

            return render_template('train.html', message="Training complete")

        except Exception as e:
            logging.error(f"{e}")
            error_message = str(e)
            return render_template('index.html', error=error_message)
        


if __name__ == '__main__':
    app.run(host='0.0.0.0', port ='8888',debug=True)