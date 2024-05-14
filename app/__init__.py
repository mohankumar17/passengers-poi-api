from flask import Flask
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes.passengers_poi import passengers_poi_bp
    app.register_blueprint(passengers_poi_bp)

    return app