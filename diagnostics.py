
import pandas as pd
import numpy as np
import timeit
import os
import json
from pathlib import Path
import logging

import ingestion as ing

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


##################Load config.json and get environment variables
with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = Path(config['output_folder_path']) 
test_data_path = Path(config['test_data_path']) 

##################Function to get model predictions
def model_predictions():
    # read the deployed model and a test dataset, calculate predictions
    return #return value should be a list containing all predictions

##################Function to get summary statistics
def dataframe_summary():
    # calculate summary statistics here
    return #return value should be a list containing all summary statistics

##################Function to get timings
def execution_time():
    # calculate timing of training.py and ingestion.py
    return #return a list of 2 timing values in seconds

##################Function to check dependencies
def outdated_packages_list():
    # get a list of 


if __name__ == '__main__':
    model_predictions()
    dataframe_summary()
    execution_time()
    outdated_packages_list()





    
