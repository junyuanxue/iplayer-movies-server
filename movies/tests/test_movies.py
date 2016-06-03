from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from unittest.mock import Mock
from movies import services

class MoviesAPITest(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_movies(self):
        mock_movies = [{'title': 'Emma', 'rating': '7/10'},
                       {'title': 'Sydney White', 'rating': '5/10'}]
        services.get_movies = Mock(return_value=mock_movies)
        response = self.client.get('/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['title'], 'Emma')
        self.assertEqual(response.json()[0]['rating'], '7/10')
        self.assertEqual(response.json()[1]['title'], 'Sydney White')
        self.assertEqual(response.json()[1]['rating'], '5/10')
