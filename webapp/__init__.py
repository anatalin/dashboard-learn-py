from flask import Flask
from flask_celeryext import FlaskCeleryExt
from flask_sqlalchemy import SQLAlchemy
from webapp.celery.celery_utils import make_celery


db = SQLAlchemy()
ext_celery = FlaskCeleryExt(create_celery_app=make_celery)

from webapp.blueprints.main import bp as main_bp
from webapp.blueprints.weather import bp as weather_bp

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    ext_celery.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(weather_bp)

    return app
