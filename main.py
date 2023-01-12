from flask import Flask
from flask_restx import Api

from config_app import Config
from const import DB
from create_db import create_form_mongo, create_form_tiny
from view.pattern import pattern_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_params(app)
    return app


def register_params(app):
    api = Api(app)
    api.add_namespace(pattern_ns)


app = create_app(Config)
create_form_tiny(DB)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
