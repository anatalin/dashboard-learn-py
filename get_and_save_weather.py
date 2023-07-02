from datetime import datetime
from webapp import create_app
from webapp.model import db, WeatherReport
from webapp.weather import get_weather

app = create_app()
with app.app_context():
    current_weather = get_weather()
    if current_weather.get('main') is not None:
        report = WeatherReport(city_name='Bishkek', 
                        temp=current_weather['main']['temp'],
                        feels_like_temp=current_weather['main']['feels_like'],
                        datetime=datetime.utcnow())
        db.session.add(report)
        db.session.commit()
