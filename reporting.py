import pickle
import pandas as pd
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
import json
import logging

import config as cfg
import data_access as da

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


############### Load config.json and get path variables
# see config.py

print(cfg.dataset_csv_path)


############## Function for reporting
def score_model(model_file, test_data_file, report_path):
    """
    Calculate a confusion matrix using the test data and the deployed model
    write the confusion matrix to the workspace.

    Parameters
    ----------
    model_file : Path
        File containing the trained ML model, that should be evaluated.

    test_data_file : Path
        File containing the test data that should be evaluated against.

    report_path : Path
        Path where the report should be placed in.
        
    Returns
    -------
    None.
    """
    json_result_file = report_path / "confusion.json"
    X, y_true = da.read_model_data(test_data_file)
    with model_file.open("rb") as fp_model:
        model = pickle.load(fp_model)
        
    # predict the test data and create the confusion matrix
    y_pred = model.predict(X)
    matrix = metrics.confusion_matrix(y_true, y_pred)
    with json_result_file.open("wt") as fp_json:
        json.dump(matrix.tolist(), fp_json)

    # plot a confusion matrix
    labels = ["exit", "stay"]
    df_confusion = pd.DataFrame(matrix, columns=labels, index=labels)
    # plt.figure(figsize=(10,7))
    # sns.set(font_scale=1.4) # for label size
    # sns.heatmap(df_confusion, annot=True, annot_kws={"size": 16}) # font size
    sns.heatmap(df_confusion, annot=True)
    plt.savefig(report_path / "confusion.png")


############## Function to perform default reporting
def perform_default_reporting():
    """
    This is what is done if the script is run from the shell.

    Returns
    -------
    None.
    """
    score_model(
        cfg.deployed_model_file, 
        cfg.test_data_file,
        cfg.report_path,
    )
    


if __name__ == '__main__':
    perform_default_reporting()