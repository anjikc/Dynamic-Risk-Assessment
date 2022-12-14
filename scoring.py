from itertools import filterfalse
from flask import Flask, session, jsonify, request
import pandas as pd
import numpy as np
import pickle
import os
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import json
from joblib import load
from functions import preprocess_data
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")



#################Load config.json and get path variables
with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['output_folder_path']) 
test_data_path = os.path.join(config['test_data_path']) 
output_folder_path = os.path.join(config['output_folder_path'])
model_path = os.path.join(config['output_model_path'])


#################Function for model scoring
def score_model(production=False):
    #this function should take a trained model, load test data, and calculate an F1 score for the model relative to the test data
    #it should write the result to the latestscore.txt file
    model = load(os.path.join(model_path, "trainedmodel.pkl"))
    encoder = load(os.path.join(model_path, "encoder.pkl"))
    
    if production :
        df = pd.read_csv(os.path.join(output_folder_path, "finaldata.csv"))
    else:
        df = pd.read_csv(os.path.join(test_data_path, "testdata.csv"))

    df_x, df_y, _ = preprocess_data(df, encoder)

    y_pred = model.predict(df_x)

    f1 = metrics.f1_score(df_y, y_pred)

    with open(os.path.join(model_path, "latestscore.txt"), "w") as score_file:
        score_file.write(str(f1) + "\n")
    
    logging.info(f"Scoring: F1={f1 :.2f}")
    
    return f1

if __name__ == '__main__':
    score_model()
