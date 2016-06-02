import requests

def get_movie_data():
    url = 'http://www.bbc.co.uk/tv/programmes/formats/films/player/episodes.json'
    response = requests.get(url)
    return response
