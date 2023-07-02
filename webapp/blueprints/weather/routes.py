from flask import render_template
from curses import flash
from webapp.blueprints.weather import bp
from webapp.data.weather_report import WeatherReport

@bp.route('/weather/<int:city_id>')
def get_weather(city_id):
    weather_report = WeatherReport.query \
                    .filter(WeatherReport.city_id == city_id) \
                    .order_by(WeatherReport.datetime.desc()) \
                    .first()
    if weather_report is None:
        flash('Не найден последний прогноз погоды')
    print(weather_report)

    return render_template('weather/weather.html', model=weather_report)
