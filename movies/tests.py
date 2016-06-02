from django.test import TestCase
from rest_framework.test import APIClient

# class ServiceTest(TestCase):

    # def test_get_movies_from_bbc_iplayer(self):


class MoviesAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_movies(self):
        response = self.client.get('/movies')
        self.assertEqual(response.status_code, "200")



if __name__ == "__main__":
    unittest.main()
