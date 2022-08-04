from app import app
import unittest
import requests
import os


class TestApp(unittest.TestCase):

    def test_imdb_api(self):
        url = f"https://imdb-api.com/en/API/Title/{os.environ.get('API_KEY')}/tt1832382"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('application/json; charset=utf-8', response.headers['content-type'])

    def test_index(self):
        app_client = app.test_client(self)
        response = app_client.get('/')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
