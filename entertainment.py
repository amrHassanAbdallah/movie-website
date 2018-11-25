import json

import fresh_tomatoes
import media


def getAllMovies():
    with open('data.json') as data_file:
        data = json.load(data_file)
    return data['movies']


movies_objs = []
movies = getAllMovies()
for movie in movies:
    movies_objs.append(media.Movie(movie['name'], movie['thumbnail'], movie['youtube_link']))
fresh_tomatoes.open_movies_page(movies_objs)
