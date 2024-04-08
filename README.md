# p3_attrition
Predict the attrition risk of customers.

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



