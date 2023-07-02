from flask import render_template
from webapp.blueprints.main import bp
from webapp.data.city import City


@bp.route('/')
def index():
    cities = City.query.order_by(City.name.asc()).all()
    model = {
        'cities': [{'id': city.id, 'name': city.name} for city in cities]
    }
    
    return render_template('main/index.html', model=model)
