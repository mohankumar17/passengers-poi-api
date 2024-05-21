import yaml

class Config:
    with open("config/dev.yaml") as config_file:
        properties = yaml.safe_load(config_file)
    
    HTTP_HOST = properties["http"]["host"]
    HTTP_PORT = properties["http"]["port"]

    IBM_COS_HOST = properties["ibm"]["COS"]["host"]
    IBM_COS_BASEPATH = properties["ibm"]["COS"]["basePath"]
    IBM_COS_INSTANCEID = properties["ibm"]["COS"]["instanceId"]

    IBM_OAUTH_URL = properties["ibm"]["OAuth"]["url"]
    IBM_OAUTH_APIKEY = properties["ibm"]["OAuth"]["apiKey"]