from io import BytesIO
import requests
from flask import send_file, current_app

from app.utils.auth_token import get_auth_token
from app.utils.custom_exception import PASSENGERS_POI_NOT_FOUND

def get_passenger_poi(bucketName, fileName):
    
    access_token = get_auth_token()

    url = f'{current_app.config.get("IBM_COS_HOST")}{current_app.config.get("IBM_COS_BASEPATH")}/{bucketName}/{fileName}'
    headers = {
        "Authorization": f"Bearer {access_token}",
        "ibm-service-instance-id": current_app.config.get("IBM_COS_INSTANCEID")
    }

    res = requests.get(url=url, headers=headers)

    if res.status_code == 200:
        return send_file(BytesIO(res.content), mimetype='image/x-png')
    elif res.status_code == 404:
        raise PASSENGERS_POI_NOT_FOUND(f"Pasenger Idetity Proof with name {fileName} is not found the Cloud Object Storage")
    else:
        raise Exception("Failed to fetch document")
    