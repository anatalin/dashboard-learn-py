from flask import Blueprint

bp = Blueprint('main', __name__)

from webapp.blueprints.main import routes
