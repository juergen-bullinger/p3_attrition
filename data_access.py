#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper functions to access the data.

Created on Tue Apr  9 14:28:18 2024

@author: juergen
"""
import pandas as pd


def read_raw_data(csv_file_name):
    """
    read the file referenced by the csv_file_name and return the raw data
    as is in a pandas dataframe

    Parameters
    ----------
    csv_file_name : TYPE
        File name and path of the csv file to read.

    Returns
    -------
    DataFrame.
    """
    return pd.read_csv(csv_file_name)   
    

def read_model_data(csv_file_name):
    """
    As read_raw_data but remove the columns not necessary for training
    and spilt-off the target column if it is present.

    Parameters
    ----------
    csv_file_name : TYPE
        File name and path of the csv file to read.

    Returns
    -------
    Tuple of DataFrame and Series (or None).
    The DataFrame contains the features and the series the target column 
    or None if there is not target column in the file.
    """
    df = read_raw_data(csv_file_name)
    if "exited" in df.columns:
        # exited is the target variable to be predicted
        target = df.pop("exited")
    else:
        target = None
    columns_to_return = [
        "lastmonth_activity", 
        "lastyear_activity",
        "number_of_employees",
    ]
    return df[columns_to_return], target
