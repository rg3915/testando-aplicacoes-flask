from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.views import page as page_blueprint


db = SQLAlchemy() # middleware


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    app.register_blueprint(page_blueprint)

    return app