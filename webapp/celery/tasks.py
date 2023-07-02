from webapp import ext_celery, create_app, db
from webapp.clients.openweathermap import get_weather
from webapp.data.city import City
from webapp.data.weather_report import WeatherReport
from datetime import datetime
from celery.schedules import crontab

app = create_app()
celery_app = ext_celery.celery


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=1), take_and_save_weather.s())


@celery_app.task
def take_and_save_weather():
    with app.app_context():
        cities = City.query.all()
        for city in cities:
            print(f'Receiving weather for city {city.name}')
            current_weather = get_weather(city.lat, city.lon)
            print(f'Weather for {city.name}: {current_weather}')
            if current_weather.get('main') is not None:
                report = WeatherReport(city_id=city.id,
                                    temp=current_weather['main']['temp'],
                                    feels_like_temp=current_weather['main']['feels_like'],
                                    datetime=datetime.utcnow())
                db.session.add(report)
                db.session.commit()
                print(f'Saved weather for city {city.name}')
