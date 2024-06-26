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
import timeit
import helpers 

###################Load config.json and get path variables
# see config.py

#################Function for training the model
def train_model():
    start_time = timeit.default_timer()
    # use this logistic regression for training
    model = LogisticRegression(
            C=1.0, 
            class_weight=None, 
            dual=False, 
            fit_intercept=True,
            intercept_scaling=1, 
            l1_ratio=None, 
            max_iter=100,
            multi_class='ovr', 
            n_jobs=None, 
            penalty='l2',
            random_state=0, 
            solver='liblinear', 
            tol=0.0001, 
            verbose=0,
            warm_start=False
    )
    # read the training data
    X, y_true = da.read_model_data(cfg.merge_result_file)
    
    # fit the logistic regression to your data
    model.fit(X, y_true)
    
    end_time = timeit.default_timer()
    helpers.log_runtime("training", end_time - start_time)
    # write the trained model to your workspace in a file called 
    # trainedmodel.pkl
    with cfg.output_model_file.open("wb") as fp_model:
        pickle.dump(model, fp_model)
    return model