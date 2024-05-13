# Insurance Price Prediction


## How To Start

### Creat Environment
```
conda create -p venv python==3.8 -y
```
### Activate Environment
```
conda activate ./env
```
### Install Requirements 
```
pip install -r requirements.txt
```

## Problem Statement

The goal of this project is to give people an estimate of how much they need based on
their individual health situation. After that, customers can work with any health
insurance carrier and its plans and perks while keeping the projected cost from our
study in mind. This can assist a person in concentrating on the health side of an
insurance policy rather than the ineffective part.



**Project Goal: Helping You Choose the Right Health Insurance**

1. **Customized Advice:** I want to give you personalized suggestions about how much health insurance you might need. This advice will be based on things like your age, health, lifestyle, and family. By offering a precise estimate, individuals can better understand their insurance needs.

2. **Easy Access to Options:** I'll make it simple for you to check out different health insurance companies and their plans. This way, you can pick the one that fits you best.


3. **Knowing Costs:**  I'll help you understand how much your insurance might cost. This will help you decide if it's worth it and if you're getting a good deal.

4. **Focus on Your Health:**  I think it's important to focus on what health benefits you'll get from your insurance. This means making sure you have enough coverage to take care of yourself when you need it most.

In short, project is all about making health insurance easier to understand and choose. I'll give you advice tailored to you, show you different options, help you understand costs, and keep your health the main focus. This way, you can pick the right insurance for you and stay healthy without worrying about money.

## Dataset:-
```
https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction
```
## Project Various Steps:-
### Data Ingestion
I started the project by carefully finding and adding data. I used Kaggle, a trusted platform with good datasets, to get the important data we needed for predicting prices. Then, I downloaded this data and stored it safely on our system. Then, I smoothly included this data into my project. This careful process sets a strong base for creating accurate price prediction models and doing detailed analysis.

### Data transformation
Steps performed in pre-processing are:
- • First read data from Artifact folder
- • Performed one-hot encoder on categorical columns.
- • Scaling is performed for needed information.
- • And, the info is prepared for passing to the machine learning formula

### Modelling
The pre-processed information is then envisioned and every one the specified insights are being drawn. though from the drawn insights, the info is at random unfold however still modelling is performed with completely different machine learning algorithms to form positive I tend to cowl all the chances. and eventually, Gradient Boosting performed well .

### Batch Prediction

In the pursuit of creating a comprehensive and efficient system, I have successfully executed batch prediction as a pivotal component of my project. Leveraging a meticulously designed data transformation pipeline, I have harnessed the power of predictive model to generate accurate and timely batch predictions. This milestone signifies the culmination of the efforts in seamlessly processing and analyzing data, resulting in actionable insights that drive informed decision-making. As I prepare the Low-Level Design Document, this achievement underscores the significance of the data transformation pipeline and predictive model, which will be elaborately detailed to ensure clarity and scalability in the system architecture.

### Training And Prediction Pipeline

In my pursuit of creating a robust end-to-end data-driven solution, I've meticulously crafted both a training pipeline and a prediction pipeline. The training pipeline serves as the backbone for developing predictive models, allowing me to iteratively train and fine-tune them with the utmost precision. Meanwhile, the prediction pipeline seamlessly applies these trained models to new data, ensuring consistently accurate insights and forecasts. This dual-pipeline approach embodies my commitment to providing a comprehensive, data-driven solution that empowers decision-makers with reliable and up-to-date information. As I delve into the creation of my Low-Level Design Document, I will intricately detail these pipelines, showcasing their sophistication and efficiency in my system architecture.

### UI Integration

Both CSS and HTML files are being created and are being integrated with the created machine learning model. All the required files are then integrated to the app.py(For localhost), Application.py(For Streamlit) file and tested locally

## Project Link - 
[Insurance Premium Prediction](https://sakshi4160-insurance-price-prediction-application-2djyvi.streamlit.app/)

