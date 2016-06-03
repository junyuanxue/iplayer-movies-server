from django.test import TestCase
import requests
from unittest.mock import Mock
from movies import services

class ServicesTest(TestCase):

    def test_get_movies_data_and_return_parsed_movies(self):
        data = {
            'episodes': [
                {
                    'programme': {
                        'title': 'Sydney White',
                        'short_synopsis': 'Modern Snow White',
                        'duration': 6060,
                        'first_broadcast_date': '2012-10-13T13:30:00+01:00',
                        'ownership': {
                            'service': {
                                'title': 'BBC Two'
                            }
                        }
                    }
                },
                {
                    'programme': {
                        'title': 'Emma',
                        'short_synopsis': 'Jane Austen classic',
                        'duration': 6840,
                        'first_broadcast_date': '2010-09-05T17:05:00+01:00',
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
        expected_result = [
            {
                'title': 'Sydney White',
                'synopsis': 'Modern Snow White',
                'duration': 101,
                'channel': 'BBC Two',
                'rating': 5
            },
            {
                'title': 'Emma',
                'synopsis': 'Jane Austen classic',
                'duration': 114,
                'channel': 'BBC Two',
                'rating': 7
            }
        ]
        movies = services.get_movies()
        print('****')
        print(movies)
        self.assertEqual(movies, expected_result)
