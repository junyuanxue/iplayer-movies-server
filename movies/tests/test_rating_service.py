from django.test import TestCase
import requests
from unittest.mock import Mock
from movies.services import rating_service

class RatingServiceTest(TestCase):

    def test_get_rating(self):
        data = {
            'results': [
                { 'vote_average': 7 }
            ]
        }
        mock_response = Mock()
        mock_response.json.return_value = data
        requests.get = Mock(return_value=mock_response)
        movie = {
            'programme': { 'title': 'Emma' }
        }
        rating = rating_service.get_rating(movie)
        self.assertEqual(rating, 7)
