from django.test import TestCase
import requests
from unittest.mock import Mock, patch
from movies import services

class ServicesTest(TestCase):

    def test_get_movies(self):
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.status_code = 200
            mock_response.content = {'title': 'Emma'}
            response = services.get_movies()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content['title'], 'Emma')
