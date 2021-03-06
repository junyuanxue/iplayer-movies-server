import requests
from movies.services import rating_service

def get_movies():
    movies_info = __get_movie_data()['episodes']
    movies = list(map(__parse_data, movies_info))
    return movies

def __get_movie_data():
    url = 'http://www.bbc.co.uk/tv/programmes/formats/films/player/episodes.json'
    response = requests.get(url)
    return response.json()

def __parse_data(info):
    rating = rating_service.get_rating(info)
    movie = {
        'title': info['programme']['title'],
        'pid': info['programme']['pid'],
        'synopsis': info['programme']['short_synopsis'],
        'duration': info['programme']['duration'],
        'rating': rating
    }
    return movie
