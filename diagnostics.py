
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
    with model_file.open("rb") as fp_model:
        model = pickle.load(fp_model)
    X, y_true = da.read_model_data(data_file)
    y_pred = model.predict(X)
    return y_pred


################## Function to get summary statistics
def dataframe_summary(data_file):
    """
    Create a list of the summary statistics each of the statistics is a dict

    Parameters
    ----------
    data_file : str or path
        Path to the csv file to be examined.

    Returns
    -------
    list of dicts (one dict per numeric columns)
    """
    df = da.read_raw_data(data_file)
    df_numeric = df.select_dtypes(include=["int", "float"])
    return [
        {
            "column": col_name,
            "mean": col_series.mean(),
            "median": col_series.median(),
            "std": col_series.std(),            
        }
        for col_name, col_series in df_numeric.items()
    ]
    

################## Function to get the summary of missing values
def missing_summary(data_file):
    """
    Create a list of ratios of missing values

    Parameters
    ----------
    data_file : str or path
        Path to the csv file to be examined.

    Returns
    -------
    list of dicts (one dict per column)
    """
    df = da.read_raw_data(data_file)
    summary = []
    for col_name, col_series in df.items():
        na_ratio = col_series.isna().mean()
        logger.info(
            "NA ratio of column %s is %s",
            col_name,
            na_ratio,
        )
        summary.append(
            {
                "column": col_name,
                "missing": na_ratio,
            }
        )
    return summary


################## Function to get timings
def execution_time():
    # calculate timing of training.py and ingestion.py
    runtimes = helpers.read_runtimes()
    logger.info("the following runtimes were measured %s", runtimes)
    return [runtimes.get("training"), runtimes.get("ingestion")]


################## Function to combine na und timing diagnostics
def diagnstics_for_missing_data_and_timing(data_file):
    """
    Prepare the combined result for missing data and timings for the
    api endpoint
    """
    result_document = {
        "missing_data": missing_summary(data_file),
        "timing_info": execution_time(),
    }


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
    outdated_packages = pip_output.splitlines()
    if outdated_packages:
        logger.info("the following packages should be checked for updates:")
        for package_line in outdated_packages:
            logger.info(package_line)
    return outdated_packages


################## Perform default diagnostics
def perform_default_diagnostics():
    """
    This is what is done if the script is run from the shell.

    Returns
    -------
    None.
    """
    model_predictions(cfg.deployed_model_file, cfg.test_data_file)
    dataframe_summary(cfg.test_data_file)
    missing_summary(cfg.test_data_file)
    execution_time()
    outdated_packages_list()
    
    

if __name__ == '__main__':
    perform_default_diagnostics()
