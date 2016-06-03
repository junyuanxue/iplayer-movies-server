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
        'duration': info['programme']['duration'] / 60,
        'channel': info['programme']['ownership']['service']['title'],
        'rating': rating
    }
    return movie

def __get_movie_rating(info):
    first_broadcast_date = info['programme']['first_broadcast_date']
    release_year = parse(first_broadcast_date).year
    title = info['programme']['title']

    base_url = 'https://api.themoviedb.org/3/search/multi'
    api_key = settings.MOVIE_DB_API_KEY
    params = '?api_key=' + api_key + '&query=' + title
    response = requests.get(base_url + params)
    potential_matches = response.json()['results']

    if len(potential_matches) == 0:
        return None
    if len(potential_matches) == 1:
        return potential_matches[0]['vote_average']
    else:
        movie = __find_match(release_year, potential_matches)
        return 'TOO MANY MOVIE OPTIONS'

def __find_match(release_year, potential_matches):
    for movie in potential_matches:
        if 'release_date' in movie:
            release_year_in_db = parse(movie['release_date']).year
            return
