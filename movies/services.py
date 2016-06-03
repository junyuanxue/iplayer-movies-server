import requests

def get_movies():
    movies_json = __get_movie_data()
    movies = map(__parse_data, movies_json['episodes'])
    return movies

def __get_movie_data():
    url = 'http://www.bbc.co.uk/tv/programmes/formats/films/player/episodes.json'
    response = requests.get(url)
    return response.json()

def __parse_data(movie_details):
    movie = {'title': movie_details['programme']['title']}
    return movie
