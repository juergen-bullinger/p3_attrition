#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
General helper functions.

Created on Tue Apr  9 22:13:27 2024

@author: juergen
"""

import json
import config as cfg

def read_runtimes():
    """
    Read the file with the runtimes and return its content as a python dict.
    Return an empty dict if it does not yet exist

    Returns
    -------
    dict.
    """
    if cfg.time_log_file.exists():
        with cfg.time_log_file.open("rt") as fp_run:
            runtimes = json.load(fp_run)
    else:
        runtimes = dict()
    return runtimes


def write_runtimes(runtimes_dict):
    """
    Write the file with the runtimes.

    Returns
    -------
    None.
    """
    with cfg.time_log_file.open("wt") as fp_run:
        json.dump(runtimes_dict, fp_run)


def log_runtime(key, runtime_in_seconds):
    """
    Update the protocol file for the runtimes for the given key.
    If the file does not exist yet, create a new one.

    Parameters
    ----------
    key : str
        Key to identify the measurment.
    runtime_in_seconds : float
        number of seconds as a float of the runtime.

    Returns
    -------
    None.
    """
    runtimes = read_runtimes()
    runtimes[key] = runtime_in_seconds
    # write the measurments back
    write_runtimes(runtimes)
