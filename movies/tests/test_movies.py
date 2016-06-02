from rest_framework import status
from rest_framework.test import APIClient, APITestCase

class MoviesAPITest(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_movies(self):
        response = self.client.get('/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
