# p3_attrition
Predict the attrition risk of customers.

## Installation
1. extract workspace.tgz in your home directory
2. make ~/workspace/src/process_cron.sh executable by
   chmod 755 ~/workspace/src/process_cron.sh
3. install the crontab by
   crontab ~/workspace/src/crontab
4. start the api
   cd ~/workspace
   python wsgi.py

## github repository url
https://github.com/juergen-bullinger/p3_attrition.git

## Directory Structure
* /home/workspace, the root directory. When you load your workspace, this is the location that will automatically load. This is also the location of many of your starter files.
* /practicedata/. This is a directory that contains some data you can use for practice.
* /sourcedata/. This is a directory that contains data that you'll load to train your models.
* /ingesteddata/. This is a directory that will contain the compiled datasets after your ingestion script.
* /testdata/. This directory contains data you can use for testing your models.
* /models/. This is a directory that will contain ML models that you create for production.
* /practicemodels/. This is a directory that will contain ML models that you create as practice.
* /production_deployment/. This is a directory that will contain your final, deployed models.

## Source Files
### fullprocess.py
Frame script that calls the other scripts to perform the full process.

### ingestion.py
Reads the csv files in the input directory and merges them to one csv file, that is then placed in ingesteddata.

### training.py
Trains a new logistic regression model.

### scoring.py
Calculates the score (f1) for the trained model and accesses the previous score, so it can be checked for improvements / model drift.

### deployment.py
Deployment of a newly trained model and the data used for training.

### diagnostics.py
Diagnostics on the data to be used in the api.

### reporting.py
Reporting on the model quality (confusion matrix).

### app.py
Rest api to use and evaluate the model and the training data.

### wsgi.py
Start the api.

### config.py
Helper script to factor out the config access and to define importable names for frequently used config values.

### helpers.py
Helper functions for storing runtime information without losing pervious measurements.
The measurements are stored to a json file.

### data_access.py
Helper functions for accessing data for training and prediction.

### data_access.py
Helper script to factor out the data access. To read and prepare the csv files.

### apicalls.py
Test of the api


# Helpfull Github commands
git config --global github.user <your_username>
then use this command

git config --global credential.helper store
