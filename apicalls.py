import requests
import logging

import config as cfg
import json

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


#Specify a URL that resolves to your workspace
URL = "http://127.0.0.1:5000/"

def log_get(*args, **kwargs):
    logger.info("calling get with args=%s and kwargs=%s", args, kwargs)
    response = requests.get(*args, **kwargs)
    logger.info("received raw response %s", response.text)
    return response

#Call each API endpoint and store the responses
responses = {}
"""
resp_predicitons = requests.post(
    f"{URL}prediction", 
    json={"data_file": str(cfg.test_data_file)}
)
"""
resp_predicitons = requests.post(
    f"{URL}prediction", 
    data={"data_file": str(cfg.test_data_file)}
)

logger.info("the response of predicition is %s", resp_predicitons)
logger.info("as text %s", resp_predicitons.text)

responses["prediction"] = resp_predicitons.json()



# read the responses for the get-type endpoints
for endpoint in ["scoring", "summarystats", "diagnostics"]:
    responses[endpoint] = log_get(f"{URL}{endpoint}").json()

#write the responses to your workspace
endpoint_json = cfg.report_path / "endpoint_responses.json"
logger.info("writing results to %s", endpoint_json)
with endpoint_json.open("wt") as fp_json:
    json.dump(responses, fp_json)

