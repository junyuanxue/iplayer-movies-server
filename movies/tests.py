from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

# class ServiceTest(TestCase):

    # def test_get_movies_from_bbc_iplayer(self):


class MoviesAPITest(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_movies(self):
        response = self.client.get('/movies/')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



if __name__ == '__main__':
    unittest.main()
