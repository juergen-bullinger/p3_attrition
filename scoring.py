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
import ast


################# Load config.json and get path variables
# see config by

print(cfg.dataset_csv_path)
print(cfg.test_data_path)


################# Function for model scoring
def score_model(model, write_score=True):
    """
    Take a trained model, load test data, and calculate an F1 score for the 
    model relative to the test data.
    Then write the result to the latestscore.txt file

    Parameters
    ----------
    model : ML Model
        A trained linear regression model.
        
    write_score : bool
        If set to True, the new score is written to the score file.

    Returns
    -------
    a tuple of 
    the model's f1 score (float)
    and the previous f1 score (float) or None if there was no previous value
    """
    # load test data
    X, y_true = da.read_model_data(cfg.test_data_file)
    
    # predict y using the given model
    y_pred = model.pred(X)
    
    # calculate an F1 score for the model relative to the test data
    model_f1_score = metrics.f1_score(y_true, y_pred)
    
    # retain the old f1 score from the previous run, if there was one
    if cfg.latest_score_file.exists():
        # the file is there, so read the old value into a variable
        with cfg.latest_score_file.open("rt") as fp_score:
            f1_score_text = fp_score.read()
            previous_model_f1_score = ast.literal_eval(f1_score_text)
    else:
        # we have no previous value (probbly this is the first run)
        previous_model_f1_score = None
    if write_score:
        # write the result to the latestscore.txt file
        with cfg.latest_score_file.open("wt") as fp_score:
            fp_score.write(str(model_f1_score))
    return model_f1_score, previous_model_f1_score

