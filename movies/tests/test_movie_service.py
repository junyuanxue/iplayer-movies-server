from django.test import TestCase
import requests
from unittest.mock import Mock, patch
from movies.services import movie_service
from movies.services import rating_service

class MovieServiceTest(TestCase):

    def test_get_movies_data_and_return_parsed_movies(self):
        data = {
            'episodes': [
                {
                    'programme': {
                        'title': 'Sydney White',
                        'pid': 'b01ngx7r',
                        'short_synopsis': 'Modern Snow White',
                        'duration': 6060
                    }
                },
                {
                    'programme': {
                        'title': 'Emma',
                        'pid': 'b007969t',
                        'short_synopsis': 'Jane Austen classic',
                        'duration': 6840
                    }
                }
            ]
        }
        with patch.object(rating_service, 'get_rating') as mock_rating_service:
            mock_rating_service.return_value = 5
            mock_response = Mock()
            mock_response.json.return_value = data
            requests.get = Mock(return_value=mock_response)
            expected_result = [
                {
                    'title': 'Sydney White',
                    'pid': 'b01ngx7r',
                    'synopsis': 'Modern Snow White',
                    'duration': 6060,
                    'rating': 5
                },
                {
                    'title': 'Emma',
                    'pid': 'b007969t',
                    'synopsis': 'Jane Austen classic',
                    'duration': 6840,
                    'rating': 5
                }
            ]
            self.assertEqual(movie_service.get_movies(), expected_result)
