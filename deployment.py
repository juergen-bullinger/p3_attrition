from flask import Flask, session, jsonify, request
import pandas as pd
import numpy as np
import pickle
import os
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import config as cfg
import data_access as da
import logging
import shutil

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()



################## Load config.json and correct path variable
# see config.py

print(cfg.dataset_csv_path)
print(cfg.prod_deployment_path)
print(cfg.merge_protocol_file)


#################### function for deployment
def store_model_into_pickle(model):
    # create the pickle file for the model
    with cfg.prod_deployment_path.open("wb") as fp:
        pickle.dump(model, fp)
    
    X, y_true = da.read_model_data(cfg.merge_result_file)
    y_pred = model.predict(X)
    
    # copy the latestscore.txt value, 
    # and the ingestfiles.txt file into the deployment directory
    shutil.copy(str(cfg.merge_protocol_path), str(cfg.prod_deployment_path))
    
        

