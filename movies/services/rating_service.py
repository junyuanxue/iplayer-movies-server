import requests
from django.conf import settings

def get_rating(info):
    response = requests.get(set_up_url(info))
    matches = response.json()['results']
    return None if matches == [] else matches[0]['vote_average']

def set_up_url(info):
    title = info['programme']['title']
    base_url = 'https://api.themoviedb.org/3/search/multi'
    api_key = settings.MOVIE_DB_API_KEY
    params = '?api_key=' + api_key + '&query=' + title
    return base_url + params
