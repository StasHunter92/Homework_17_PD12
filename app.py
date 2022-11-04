from flask import Flask, request
from flask_restx import Api, Resource
from classes.db_classes import db, Movie, Director, Genre
from schemas.db_schemas import movie_schema, movies_schema, director_schema, directors_schema, genre_schema, \
    genres_schema
from utils.create_db import create_database
from utils.utils import add_object_to_database, delete_object_from_database
# ----------------------------------------------------------------------------------------------------------------------

# Create app instance
app = Flask(__name__)
app.config.from_pyfile("config.py")
db.init_app(app)

# Initialize RESTX
api = Api(app)

# Create database
create_database(app)

# Create namespaces
movie_ns = api.namespace('movies')
director_ns = api.namespace('directors')
genre_ns = api.namespace('genres')
# ----------------------------------------------------------------------------------------------------------------------


# Main routes
@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id: str = request.args.get('director_id')
        genre_id: str = request.args.get('genre_id')
        page: str = request.args.get('page')

        if director_id and genre_id:
            movies = db.session.query(Movie).filter_by(director_id=director_id, genre_id=genre_id).all()
            if movies:
                return movies_schema.dump(movies), 200
            return "Movies not found", 404

        if director_id:
            movies = db.session.query(Movie).filter_by(director_id=director_id).all()
            if movies:
                return movies_schema.dump(movies), 200
            return "Movies not found", 404

        if genre_id:
            movies = db.session.query(Movie).filter_by(genre_id=genre_id).all()
            if movies:
                return movies_schema.dump(movies), 200
            return "Movies not found", 404

        if page:
            try:
                movies = db.session.query(Movie).limit(5).offset((int(page) - 1) * 5).all()
                return movies_schema.dump(movies), 200
            except ValueError:
                return "Page number is not integer", 404

        all_movies = Movie.query.all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        data = request.json
        try:
            new_movie = Movie(**data)
            add_object_to_database(new_movie)
            return "Movie added", 201
        except TypeError:
            return "Invalid fields", 500


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id):
        movie = Movie.query.get(movie_id)
        if movie:
            return movie_schema.dump(movie), 200
        return "Invalid id", 404

    def put(self, movie_id):
        data = request.json
        movie = Movie.query.get(movie_id)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        add_object_to_database(movie)
        return "", 204

    def patch(self, movie_id):
        data = request.json
        movie = Movie.query.get(movie_id)

        if "title" in data:
            movie.title = data.get("title")
        if "description" in data:
            movie.description = data.get("description")
        if "trailer" in data:
            movie.trailer = data.get("trailer")
        if "year" in data:
            movie.year = data.get("year")
        if "rating" in data:
            movie.rating = data.get("rating")
        if "genre_id" in data:
            movie.genre_id = data.get("genre_id")
        if "director_id" in data:
            movie.director_id = data.get("director_id")

        add_object_to_database(movie)
        return "", 204

    def delete(self, movie_id):
        movie = Movie.query.get(movie_id)
        delete_object_from_database(movie)
        return "", 204


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = Director.query.all()
        return directors_schema.dump(all_directors), 200

    def post(self):
        data = request.json
        try:
            new_director = Director(**data)
            add_object_to_database(new_director)
            return "Director added", 201
        except TypeError:
            return "Invalid fields", 500


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    def get(self, director_id):
        director = Director.query.get(director_id)
        if director:
            return director_schema.dump(director), 200
        return "Invalid id", 500

    def put(self, director_id):
        data = request.json
        director = Director.query.get(director_id)

        director.name = data.get('name')

        add_object_to_database(director)
        return "", 204

    def patch(self, director_id):
        data = request.json
        director = Director.query.get(director_id)

        if "name" in data:
            director.name = data.get("name")

        add_object_to_database(director)
        return "", 204

    def delete(self, director_id):
        director = Director.query.get(director_id)
        delete_object_from_database(director)
        return "", 204


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = Genre.query.all()
        return genres_schema.dump(all_genres), 200

    def post(self):
        data = request.json
        try:
            new_genre = Genre(**data)
            add_object_to_database(new_genre)
            return "Genre added", 201
        except TypeError:
            return "Invalid fields", 500


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id):
        genre = Genre.query.get(genre_id)
        if genre:
            return genre_schema.dump(genre), 200
        return "Invalid id", 500

    def put(self, genre_id):
        data = request.json
        genre = Genre.query.get(genre_id)

        genre.name = data.get('name')

        add_object_to_database(genre)
        return "", 204

    def patch(self, genre_id):
        data = request.json
        genre = Genre.query.get(genre_id)

        if "name" in data:
            genre.name = data.get("name")

        add_object_to_database(genre)
        return "", 204

    def delete(self, genre_id):
        genre = Genre.query.get(genre_id)
        delete_object_from_database(genre)
        return "", 204
# ----------------------------------------------------------------------------------------------------------------------


# Error handlers
@app.errorhandler(404)
def error_404(error):
    """Page 404 error"""
    return f"OOPS! Error {error}, page not found", 404


@app.errorhandler(500)
def error_500(error):
    """Internal server error"""
    return f"OOPS! Error {error}, server have a problem", 500

# ----------------------------------------------------------------------------------------------------------------------


# Run app
if __name__ == '__main__':
    app.run()
