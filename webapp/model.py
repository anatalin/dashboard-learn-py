from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class WeatherReport(db.Model):
    __tablename__ = 'weather_reports'
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String, nullable=False)
    temp = db.Column(db.Float, nullable=False)
    feels_like_temp = db.Column(db.Float, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)

def __repr__(self):
    return f'<WeatherReport {self.city_name} {self.datetime}>'