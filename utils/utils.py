from flask import json

from classes.db_classes import db, Movie, Director, Genre
from config import MOVIES_PATH, DIRECTORS_PATH, GENRES_PATH


# ----------------------------------------------------------------------------------------------------------------------


def open_json_file(file) -> json:
    """
    Returns loaded JSON file
    :param file: JSON file to open
    """
    with open(file, encoding="utf-8") as file:
        return json.load(file)


def add_movies_to_database() -> list:
    """
    Add movie object to a list of movies
    :return: list of movies
    """
    movies = open_json_file(MOVIES_PATH)
    movies_list = []

    for movie in movies:
        movie_to_add = Movie(
            id=movie.get("pk"),
            title=movie.get("title"),
            description=movie.get("description"),
            trailer=movie.get("trailer"),
            year=movie.get("year"),
            rating=movie.get("rating"),
            genre_id=movie.get("genre_id"),
            director_id=movie.get("director_id")
        )
        movies_list.append(movie_to_add)

    return movies_list


def add_directors_to_database() -> list:
    """
    Add director object to a list of directors
    :return: list of directors
    """
    directors = open_json_file(DIRECTORS_PATH)
    directors_list = []

    for director in directors:
        director_to_add = Director(
            id=director.get("pk"),
            name=director.get("name")
        )
        directors_list.append(director_to_add)

    return directors_list


def add_genres_to_database() -> list:
    """
    Add genre object to a list of genres
    :return: list of genres
    """
    genres = open_json_file(GENRES_PATH)
    genres_list = []

    for genre in genres:
        genre_to_add = Genre(
            id=genre.get("pk"),
            name=genre.get("name")
        )
        genres_list.append(genre_to_add)

    return genres_list


def add_object_to_database(data) -> None:
    """
    Add class instance to database
    :param data: class instance
    :return: None
    """
    db.session.add(data)
    db.session.commit()


def delete_object_from_database(data) -> None:
    """
    Delete class instance from database
    :param data: class instance
    :return: None
    """
    db.session.delete(data)
    db.session.commit()
