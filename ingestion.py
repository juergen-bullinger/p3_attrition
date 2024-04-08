import pandas as pd
import numpy as np
import os
import json
from datetime import datetime
from pathlib import Path




#############Load config.json and get input and output paths
with open('config.json','r') as f:
    config = json.load(f) 

input_folder_path = Path(config['input_folder_path'])
output_folder_path = Path(config['output_folder_path'])



#############Function for data ingestion
def read_and_concat_csv(path):
    """
    Read and concat the files in the given path

    Parameters
    ----------
    path : Path or str
        Path to the directory in which the csv files reside.

    Returns
    -------
    DataFrame.
    """
    data_frames_to_merge = []
    for input_file in path.glob("*.csv"):
        print(f"reading {input_file}...")
        df = pd.read_csv(input_file)
        data_frames_to_merge.append(df)
    return pd.concat(data_frames_to_merge)

    
def merge_multiple_dataframe(input_path, output_file):
    """
    Merge the files in the input folder and write the merged result to the 
    output folder.
    """
    #check for datasets, compile them together, and write to an output file
    merged_df = read_and_concat_csv(input_path)
    merged_df.to_csv(output_file)
    
    

if __name__ == '__main__':
    merge_multiple_dataframe(
        input_folder_path, 
        output_folder_path / "merged.csv"
    )
