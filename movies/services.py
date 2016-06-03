import requests

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
    duration = __format_duration(info['programme']['duration'])
    movie = {
        'title': info['programme']['title'],
        'synopsis': info['programme']['short_synopsis'],
        'duration': duration,
        'channel': info['programme']['ownership']['service']['title'],
        'rating': rating
    }
    return movie

def __format_duration(seconds):
    duration_minutes = int(seconds / 60)
    return '{} minutes'.format(duration_minutes)

def __get_movie_rating(info):
    release_year = info['programme']['first_broadcast_date']
    return '*/10'
