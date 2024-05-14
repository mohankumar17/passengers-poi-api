from app.config import Config
from datetime import datetime, timedelta
from urllib.parse import urlencode
import os
import requests

def get_auth_token():

    current_time = datetime.now()
    expiry_time = os.environ.get("ACCESS_TOKEN_EXPIRY_TIME")

    if expiry_time is not None and str(current_time) < expiry_time:
        return os.environ.get("ACCESS_TOKEN")

    url = Config.IBM_OAUTH_URL
    body = urlencode({
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": Config.IBM_OAUTH_APIKEY
    })

    res = requests.post(url=url, data=body)

    if res.status_code == 200:
        os.environ["ACCESS_TOKEN"] = res.json().get("access_token")
        os.environ["ACCESS_TOKEN_EXPIRY_TIME"] = str(current_time + timedelta(hours=1))
        
        return os.environ.get("ACCESS_TOKEN")
    else:
        raise Exception("IBM Cloud Object Storage Authentication Failed!!")
