"""
Perform the full process
- Ingestion
- Training
- Scoring
- Deploying an ML Model

Author:
    Jürgen Bullinger
"""

import training
import scoring
import deployment
import diagnostics
import reporting
import ingestion
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


################## Check and read new data
# first, read ingestedfiles.txt
# second, determine whether the source data folder has files that aren't listed
# in ingestedfiles.txt
# This is done in ingestion.py
new_files_found = ingestion.process_new_files()


################## Deciding whether to proceed, part 1
# if you found new data, you should proceed. otherwise, do end the process here
if not new_files_found():
    # no new data found
    logger.info("now new data was found in the input directory")
    logger.info("exiting because retraining is not necessary")
    exit(0)


################## Checking for model drift
# check whether the score from the deployed model is different from the score 
# from the model that uses the newest ingested data
model = 

################## Deciding whether to proceed, part 2
# if you found model drift, you should proceed. otherwise, do end the process
# here



################## Re-deployment
# if you found evidence for model drift, re-run the deployment.py script

################## Diagnostics and reporting
# run diagnostics.py and reporting.py for the re-deployed model







