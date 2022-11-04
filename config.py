import os
# ----------------------------------------------------------------------------------------------------------------------

MOVIES_PATH = os.path.join('data', 'movies.json')
DIRECTORS_PATH = os.path.join('data', 'directors.json')
GENRES_PATH = os.path.join('data', 'genres.json')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
JSON_AS_ASCII = False
DEBUG = True
JSONIFY_PRETTYPRINT_REGULAR = True
RESTX_JSON = {'ensure_ascii': False, 'indent': 4}
