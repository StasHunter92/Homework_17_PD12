from classes.db_classes import db
from utils.utils import add_movies_to_database, add_directors_to_database, add_genres_to_database
# ----------------------------------------------------------------------------------------------------------------------


def create_database(app) -> None:
    """
    Create a new database
    :param app: the application object
    :return: None
    """
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.add_all(add_movies_to_database())
        db.session.add_all(add_directors_to_database())
        db.session.add_all(add_genres_to_database())
        db.session.commit()
