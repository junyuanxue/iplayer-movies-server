from django.test import TestCase
import requests
from unittest.mock import Mock, patch
from movies import services

class ServicesTest(TestCase):

    def test_get_movies(self):
        data = {
            'episodes': [
                {
                    'programme': {
                        'title': 'Emma',
                        'short_synopsis': 'Jane Austen classic',
                        'duration': 6840,
                        'first_broadcast_date': '2013-07-25T12:10:00+01:00',
                        'ownership': {
                            'service': {
                                'title': 'BBC Two'
                            }
                        }
                    }
                }
            ]
        }
        mock_response = Mock()
        mock_response.json.return_value = data
        requests.get = Mock(return_value=mock_response)
        expected_result = [{
            'title': 'Emma',
            'synopsis': 'Jane Austen classic',
            'duration': '114 minutes',
            'channel': 'BBC Two',
            'rating': '7/10'
        }]
        movies = services.get_movies()
        self.assertEqual(movies, expected_result)

        # with patch.object(requests, 'get') as get_mock:
