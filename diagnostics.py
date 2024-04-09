
import logging
import pickle
import subprocess

import config as cfg
import data_access as da
import helpers 

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


################## Load config.json and get environment variables
# see config.py


################## Function to get model predictions
def model_predictions(model_file, data_file):
    # read the deployed model and a test dataset, calculate predictions
    # create the pickle file for the model
    with model_file.open("wb") as fp_model:
        model = pickle.load(fp_model)
    X, y_true = da.read_model_data(data_file)
    y_pred = model.predict(X)
    return y_pred


################## Function to get summary statistics
def dataframe_summary(data_file):
    # calculate summary statistics here
    return #return value should be a list containing all summary statistics


################## Function to get timings
def execution_time():
    # calculate timing of training.py and ingestion.py
    runtimes = helpers.read_runtimes()
    return [runtimes.get("training"), runtimes.get("ingestion")]


################## Function to check dependencies
def outdated_packages_list():
    """
    Get the list of outdated packages using a subprocess call into pip

    Returns
    -------
    list
        of outdated packages.
    """
    process_handle = subprocess.run(
        ["pip", "list", "--outdated"], 
        capture_output=True,
    )
    pip_output = process_handle.stdout.decode("utf8")
    return pip_output.splitlines()


if __name__ == '__main__':
    model_predictions(cfg.deployed_model_file, cfg.test_data_file)
    dataframe_summary(cfg.test_data_file)
    execution_time()
    outdated_packages_list()
