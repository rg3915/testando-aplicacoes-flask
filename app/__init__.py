from flask import Flask
from app.views import page as page_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(page_blueprint)

    return app