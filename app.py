from flask import Flask, session, jsonify, request
import pickle
import logging
from pathlib import Path

import config as cfg
import diagnostics
import scoring

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


######################Set up variables for use in our script
app = Flask(__name__)
app.secret_key = '1652d576-484a-49fd-913a-6879acfa6ba4'


############### Load config.json and get path variables
# see config.py

print(cfg.dataset_csv_path)


# restore the deployed model
with cfg.deployed_model_file.open("rb") as fp_model:
    prediction_model = pickle.load(fp_model)


####################### Prediction Endpoint
@app.route("/prediction", methods=['POST','OPTIONS'])
def predict():
    """
    Predict using the implementation in diagnostics.py
    """
    logger.info("prediction api was called")
    data_file = Path(request.form['data_file'])
    logger.info("prediction api was called with path %s", data_file)
    if data_file.exists():
        predictions = diagnostics.model_predictions(
            cfg.deployed_model_file, 
            cfg.test_data_file,
        )
        # call the prediction function you created in Step 3
        return jsonify(predictions.tolist())
    else:
        logger.error("File %s not found", data_file)
        return jsonify(None)


####################### Scoring Endpoint
@app.route("/scoring", methods=['GET','OPTIONS'])
def scoring_endpoint():
    """
    Return the f1 score of the model.

    Returns
    -------
    str
        f1 score of the model (float converted to string).

    """
    # restore the deployed model
    logger.info("scoring api was called")        
    current_f1_score, previous_f1_score = scoring.score_model(
        prediction_model,
        write_score=False,
    )
    return jsonify(current_f1_score)


####################### Summary Statistics Endpoint
@app.route("/summarystats", methods=['GET','OPTIONS'])
def stats_endpoint():
    """
    Return the column stats as a json string.

    Returns
    -------
    str
        json list of documents (one document per column).

    """
    #check means, medians, and modes for each column
    logger.info("stats api was called")
    summary = diagnostics.dataframe_summary(cfg.merge_result_file)
    return jsonify(summary)


####################### Diagnostics Endpoint
@app.route("/diagnostics", methods=['GET','OPTIONS'])
def diagnostics_endpoint():
    # check timing and percent NA values
    logger.info("diagnostics api was called")
    summary = diagnostics.diagnstics_for_missing_data_and_timing(
        cfg.merge_result_file
    )
    return jsonify(summary)


if __name__ == "__main__":    
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
