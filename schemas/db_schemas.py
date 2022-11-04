from marshmallow import Schema, fields
# ----------------------------------------------------------------------------------------------------------------------


class MovieSchema(Schema):
    """Schema for movie"""
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


class DirectorSchema(Schema):
    """Schema for director"""
    id = fields.Int(dump_only=True)
    name = fields.Str()


class GenreSchema(Schema):
    """Schema for genre"""
    id = fields.Int(dump_only=True)
    name = fields.Str()
# ----------------------------------------------------------------------------------------------------------------------


# Class instance for all schemas
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
