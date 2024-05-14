from flask import Blueprint, request
import time
import uuid
from app.config import Config

from app.utils.custom_exception import PASSENGERS_POI_NOT_FOUND, MIMETYPE_NOT_SUPPORTED
from app.services.passenger_poi_fetch import get_passenger_poi
from app.services.passenger_poi_upload import upload_passenger_poi

passengers_poi_bp = Blueprint('passengers_poi', __name__)
logger = Config.logger

# Routers
@passengers_poi_bp.get("/api/passengers/fetch/<bucketName>/<fileName>/")
def get_passenger_poi_route(bucketName, fileName):
    return get_passenger_poi(bucketName, fileName)

@passengers_poi_bp.put("/api/passengers/upload/")
def upload_passenger_poi_route():
    return upload_passenger_poi(request)

############################################################################
'''
Error Handling
    - Global Error Handler: 500
    - Bad Request: 400
    - Not Found: 404
    - Unsupported Media Type: 415
'''
# Error Handling 
def error_response(errorDetails):
    error_response =  {
        "message": errorDetails.get("message"),
        "description": errorDetails.get("description"),
        "dateTime": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime()),
        "transactionId": str(uuid.uuid4())
    }
    logger.error(error_response)
    return error_response

@passengers_poi_bp.errorhandler(Exception)
def global_error_handler(error):
    errorDetails = {
        "message": "Passengers POI system server error",
        "description": str(error)
    }
    status_code = 500
    response = error_response(errorDetails)
    return response, status_code

@passengers_poi_bp.errorhandler(PASSENGERS_POI_NOT_FOUND)
def not_found_error_handler(error):
    errorDetails = {
        "message": "Passengers POI documents not found",
        "description": str(error)
    }
    status_code = 404
    response = error_response(errorDetails)
    return response, status_code

@passengers_poi_bp.errorhandler(MIMETYPE_NOT_SUPPORTED)
def mediatype_error_handler(error):
    errorDetails = {
        "message": "Unsupported Media Type",
        "description": str(error)
    }
    status_code = 415
    response = error_response(errorDetails)
    return response, status_code

'''@passengers_poi_bp.errorhandler()
def validation_error_handler(error):
    errorDetails = {
        "message": "Input data validation failed",
        "description": str(error)
    }
    status_code = 400
    response = error_response(errorDetails)
    return response, status_code'''
