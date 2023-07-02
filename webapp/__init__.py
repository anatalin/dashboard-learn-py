from flask import Flask, render_template
from webapp.weather import get_weather
from webapp.model import db, WeatherReport

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")
    def hello():
        return "Привет!"

    @app.route("/weather")
    def weather():
        current_weather = get_weather()
        if current_weather.get('main') is not None:
            model = {
                'temp_c': current_weather['main']['temp'],
                'temp_feels_c': current_weather['main']['feels_like'],
            }
        else:
            model = {
                'error': current_weather
            }

        return render_template("weather.html", model = model)
    
    @app.route("/weather-from-db")
    def weather_from_db():
        last_report = WeatherReport.query.order_by(WeatherReport.datetime.desc()).first()
        if last_report is not None:
            model = {
                'temp_c': last_report.temp,
                'temp_feels_c': last_report.feels_like_temp,
                'taken_at': last_report.datetime
            }
        else:
            model = {
                'error': 'Не найдены записи в БД'
            }

        return render_template('weather_from_db.html', model = model)
        
    return app