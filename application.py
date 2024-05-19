import streamlit as st
import pandas as pd
from src.InsurancePricePrediction.pipelines.prediction_pipeline import CustomData, PredictionPipeline
import os
from batch.batch import BatchPrediction
from src.InsurancePricePrediction.logger import logging
from src.InsurancePricePrediction.components.data_transformation import DataTransformationConfig
from src.InsurancePricePrediction.config.configuration import *
from src.InsurancePricePrediction.pipelines.training_pipeline import Train
from werkzeug.utils import secure_filename
import base64


transformer_file_path = os.path.join("artifacts","preprocessor.pkl")
model_file_path = os.path.join("artifacts","model.pkl")


UPLOAD_FOLDER = 'Batch_Prediction/UPLOAD_CSV_FILE'
#predicted_file_path = 'batch_prediction/Predicted_CSV_FILE/predicted_results.csv'


# Set the title of the Streamlit app
st.title("Insurance Premium Prediction App")

ALLOWED_EXTENSIONS = {'csv'}

# Streamlit sidebar
st.sidebar.header("Navigation")
selected_page = st.sidebar.radio("Select a Page", ["Home","Predict","Batch Prediction","Train"])

if selected_page == "Home":
    st.header("Home Page")
    st.write("Welcome to Insurance Premium Prediction App!")
    st.write("Use the sidebar to navigate to different pages.")
    
elif selected_page == "Train":
    st.header("Model Training")

    if st.button("Train Model"):
        try:
            pipeline = Train()
            pipeline.main()
            st.success("Training complete")
        except Exception as e:
            logging.error(f"{e}")
            st.error(f"Error during training: {str(e)}")
            

elif selected_page == "Predict":
    st.header("Single Data Point Prediction")
    
    # Create input form
    
    st.subheader("Predict Single Data Point")
    age = st.number_input("Age", min_value=0,max_value=100)
    sex = st.selectbox("Sex", ["male", "female"])
    smoker = st.selectbox("Smoker", ["yes", "no"])
    children = st.number_input("Children", min_value=0,max_value=10)
    bmi = st.number_input("BMI", min_value=0.0)
    region = st.selectbox("Region", ["Southeast","Southwest", "Northwest", "Northeast"]) 
    # Make a prediction
    if st.button("Predict"):
        data = CustomData(
            sex=sex,
            smoker=smoker,
            children=children,
            age=age,
            region=region,
            bmi=bmi
            
        )
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictionPipeline()
        pred = predict_pipeline.predict(final_new_data)
        result = int(pred[0])
        st.success(f"Predicted Insurance Premium is: {result}")

elif selected_page == "Batch Prediction":
     st.header("Batch Prediction")

     # Create a file uploader
     st.subheader("Upload a CSV File")
     uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

     if uploaded_file is not None:
         # Save the uploaded file
         file_path = os.path.join(UPLOAD_FOLDER, secure_filename(uploaded_file.name))
         with open(file_path, "wb") as f:
             f.write(uploaded_file.read())
        
         logging.info("CSV received and Uploaded")

         # Perform batch prediction using the uploaded file
         batch = BatchPrediction(file_path, model_file_path, transformer_file_path)
         batch.start_batch_prediction()

       

         # After batch prediction and displaying the success message, add a download button for the predicted file
         output = "Batch Prediction Done"
         st.success(output)

      


# Run the Streamlit app
if __name__ == '__main__':
    st.sidebar.title("My Streamlit App")
    st.title("Main Content")