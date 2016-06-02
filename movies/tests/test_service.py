from django.test import TestCase
import requests
from unittest.mock import Mock, patch
from movies import service

class ServiceTest(TestCase):

    def test_get_movie_data(self):
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.status_code = 200
            mock_response.content = {'title': 'Emma'}
            url = 'http://www.bbc.co.uk/tv/programmes/formats/films/player/episodes.json'
            response = service.get_data(url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content['title'], 'Emma')
