from flask import Blueprint

bp = Blueprint('weather', __name__)

from webapp.blueprints.weather import routes
