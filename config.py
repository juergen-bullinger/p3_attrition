#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Read the configuration from json and define some variables for quick access
to values that are used often.

Created on Tue Apr  9 14:07:34 2024

@author: juergen
"""

import json
# from datetime import datetime
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


#############Load config.json and get input and output paths
with open('config.json','r') as f:
    config = json.load(f) 

# directories
input_folder_path = Path(config['input_folder_path'])
output_folder_path = Path(config['output_folder_path'])
dataset_csv_path = Path(config['output_folder_path']) 
prod_deployment_path = Path(config['prod_deployment_path']) 
test_data_path = Path(config['test_data_path']) 
output_model_path = Path(config['output_model_path']) 


# files
merge_result_file = output_folder_path / "finaldata.csv"
merge_protocol_file = output_folder_path / "ingestedfiles.txt"
latest_score_file = prod_deployment_path / "latestscore.txt"
deployed_score_file = prod_deployment_path / "latestscore.txt"
deployed_model_file = prod_deployment_path / "trainedmodel.pkl"
output_model_file = output_model_path / "trainedmodel.pkl"
test_data_file = test_data_path / "testdata.csv"
time_log_file = output_folder_path / "runtimes.json"
