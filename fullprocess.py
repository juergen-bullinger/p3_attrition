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
if not new_files_found:
    # no new data found
    logger.info("now new data was found in the input directory")
    logger.info("exiting because retraining is not necessary")
    exit(0)


################## Checking for model drift
# check whether the score from the deployed model is different from the score 
# from the model that uses the newest ingested data
model = training.train_model()

new_score, previous_score = scoring.score_model(model, write_score=True)

################## Deciding whether to proceed, part 2
# if you found model drift, you should proceed. otherwise, do end the process
# here
if previous_score is not None and new_score == previous_score:
    logging.info(
        "the scores of the old and the new model are equal %f",
        new_score
    )
    logging.info("skipping the deployment of the new model")
    exit(0)


################## Re-deployment
# if you found evidence for model drift, re-run the deployment.py script
deployment.store_model_into_pickle(model)


################## Diagnostics and reporting
# run diagnostics.py and reporting.py for the re-deployed model
diagnostics.perform_default_diagnostics()
reporting.perform_default_reporting()







