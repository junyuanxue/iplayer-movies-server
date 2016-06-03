from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from unittest.mock import patch
from movies import services

class MoviesAPITest(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_movies(self):
        with patch.object(services, 'get_movies') as mock_services:
            mock_movies = [{'title': 'Emma', 'rating': 7},
                           {'title': 'Sydney White', 'rating': 5}]
            mock_services.return_value = mock_movies
            response = self.client.get('/movies/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.json()[0]['title'], 'Emma')
            self.assertEqual(response.json()[0]['rating'], 7)
            self.assertEqual(response.json()[1]['title'], 'Sydney White')
            self.assertEqual(response.json()[1]['rating'], 5)
