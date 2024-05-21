from flask import Flask
import logging
from app.configuration import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.logger.setLevel(logging.INFO)

    from app.routes.passengers_poi import passengers_poi_bp
    app.register_blueprint(passengers_poi_bp)

    return app