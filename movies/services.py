import requests
from dateutil.parser import parse
from django.conf import settings

def get_movies():
    movies_info = __get_movie_data()['episodes']
    movies = list(map(__parse_data, movies_info))
    return movies

def __get_movie_data():
    url = 'http://www.bbc.co.uk/tv/programmes/formats/films/player/episodes.json'
    response = requests.get(url)
    return response.json()

def __parse_data(info):
    rating = __get_movie_rating(info)
    movie = {
        'title': info['programme']['title'],
        'synopsis': info['programme']['short_synopsis'],
        'duration': info['programme']['duration'],
        'channel': info['programme']['ownership']['service']['title'],
        'rating': rating
    }
    return movie

def __get_movie_rating(info):
    title = info['programme']['title']
    base_url = 'https://api.themoviedb.org/3/search/multi'
    api_key = settings.MOVIE_DB_API_KEY
    params = '?api_key=' + api_key + '&query=' + title
    response = requests.get(base_url + params)
    matches = response.json()['results']
    return None if matches == [] else matches[0]['vote_average']
