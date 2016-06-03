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
    movie = {
        'title': info['programme']['title'],
        'synopsis': info['programme']['short_synopsis'],
        'duration': info['programme']['duration'],
        'channel': info['programme']['ownership']['service']['title'],
        'rating': rating
    }
    return movie
