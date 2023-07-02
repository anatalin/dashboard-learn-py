from webapp import db, create_app
from webapp.data.city import City
from sqlalchemy.exc import SQLAlchemyError


def fill_cities():
    cities = [
        {'name': 'Бишкек', 'lat': 42.829852, 'lon': 74.562654},
        {'name': 'Стамбул', 'lat': 41.036926, 'lon': 28.984968},
        {'name': 'Аланья', 'lat': 36.536574, 'lon': 31.998763}
    ]
    db.session.bulk_insert_mappings(City, cities)
    try:
        db.session.commit()
        print('Данные сохранены в БД')
    except SQLAlchemyError:
        db.session.rollback()
        raise


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        fill_cities()
