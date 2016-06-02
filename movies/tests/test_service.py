from django.test import TestCase
import requests
import mock

class ServiceTest(TestCase):
    def get_data(self, url):
        response = requests.get(url)
        return response

    def test_get_movie_data(self):
        with mock.patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = mock.Mock()
            mock_response.status_code = 200
            mock_response.content = {'title': 'Emma'}
            url = 'http://www.bbc.co.uk/tv/programmes/formats/films/player/episodes.json'
            response = self.get_data(url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content['title'], 'Emma')
