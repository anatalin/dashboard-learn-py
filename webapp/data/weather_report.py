from webapp import db
from webapp.data.city import City
from sqlalchemy import ForeignKey


class WeatherReport(db.Model):
    __tablename__ = 'weather_reports'
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, ForeignKey(City.id),
                        index=True, nullable=False)
    temp = db.Column(db.Float, nullable=False)
    feels_like_temp = db.Column(db.Float, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)


def __repr__(self):
    return f'<WeatherReport {self.city_name} {self.datetime}>'
