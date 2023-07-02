import requests
from flask import current_app


def get_weather(lat, lon):
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": str(lat),
        "lon": str(lon),
        "appid": current_app.config['OWM_KEY'],
        "units": "metric"
    }

    try:
        result = requests.get(weather_url, params)
        return result.json()
    except (requests.RequestException) as e:
        return f'{type(e)}: {e}'
