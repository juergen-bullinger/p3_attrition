"""
Ingest the data from the input_folder_path and create one merged result file
in output_folder_path named finaldata.csv

Author:
    Jürgen Bullinger
"""
import pandas as pd
import json
# from datetime import datetime
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


#############Load config.json and get input and output paths
with open('config.json','r') as f:
    config = json.load(f) 

input_folder_path = Path(config['input_folder_path'])
output_folder_path = Path(config['output_folder_path'])

merge_result_path = output_folder_path / "finaldata.csv"
merge_protocol_path = input_folder_path / "ingestedfiles.txt"


#############Function for data ingestion
def merge_multiple_dataframe(
        input_path, 
        output_file,
        protocol_file
    ):
    """
    Read and concat the files in the given path

    Parameters
    ----------
    input_path : Path
        Path to the directory in which the csv files reside.

    output_file : Path or str
        Path to the file which will contain the merged data.
        
    protocol_file : Path
        Path to the file which will contain the processed input files.
        
    Returns
    -------
    True if new files were found and False otherwise.
    """
    data_frames_to_merge = []
    # read the previously processed files to see if new files arived since the
    # last run
    processed_files = set()
    new_files_found = False
    if protocol_file.exists():
        with protocol_file.open("rt") as fp_in:
            processed_files.update(fp_in.read().splitlines())
        print("\n".join(processed_files))
    with protocol_file.open("wt") as fp_in:
        for input_file in input_path.glob("*.csv"):
            print(f"reading {input_file}...")
            df = pd.read_csv(input_file)
            data_frames_to_merge.append(df)
            fp_in.writeline(str(input_file))
            if str(input_file) not in processed_files:
                new_files_found = True
    if new_files_found:
        # only update if new files were found
        merged_df = pd.concat(data_frames_to_merge)
        merged_df.drop_duplicates(inplace=True)
        merged_df.to_csv(output_file)
    return new_files_found
    

def process_new_files():
    """
    Process the input folder, check for new files and if there are some
    update the output file-

    Returns
    -------
    True if there are new files, False otherwise.

    """
    return merge_multiple_dataframe(
        input_folder_path,
        merge_result_path,
        merge_protocol_path,
    )



if __name__ == '__main__':
    process_new_files()