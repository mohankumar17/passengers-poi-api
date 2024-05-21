from flask import current_app
import requests
from time import localtime, strftime
import base64

from app.utils.auth_token import get_auth_token

from app.utils.custom_exception import MIMETYPE_NOT_SUPPORTED

def upload_passenger_poi(request):
    if request.is_json:
        req_body = request.json
    else:
        raise MIMETYPE_NOT_SUPPORTED("Mediatype is not supported")
    
    document = req_body.get("document")
    bucketName = req_body.get("bucketName")
    fileName = req_body.get("fileName")
    
    body = base64.b64decode(document)
    access_token = get_auth_token()

    url = f'{current_app.config.get("IBM_COS_HOST")}{current_app.config.get("IBM_COS_BASEPATH")}/{bucketName}/{fileName}'
    headers = {
        "Authorization": f"Bearer {access_token}",
        "ibm-service-instance-id": current_app.config.get("IBM_COS_INSTANCEID")
    }

    res = requests.put(url=url, data=body, headers=headers)

    if res.status_code == 200 or res.status_code == 201:
        return {
            "message": "Document uploaded successfully",
            "bucketName": bucketName,
            "reservationId": fileName,
            "dateTime": strftime("%Y-%m-%dT%H:%M:%SZ", localtime())
        }
    else:
        raise Exception("Document upload failed")