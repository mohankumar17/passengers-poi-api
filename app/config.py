import yaml
import logging

class Config:
    with open("config/dev.yaml") as config_file:
        properties = yaml.safe_load(config_file)
    
    HTTP_HOST = properties["http"]["host"]
    HTTP_PORT = properties["http"]["port"]

    S3_HOST = properties["ibm"]["S3"]["host"]
    S3_BASEPATH = properties["ibm"]["S3"]["basePath"]
    S3_INSTANCEID = properties["ibm"]["S3"]["instanceId"]
    S3_OAUTH = properties["ibm"]["S3"]["url"]
    S3_APIKEY = properties["ibm"]["S3"]["apiKey"]

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)