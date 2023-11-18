import requests
from scraper_interface import Scraper


class HackerrankScraper(Scraper):
    def __init__(self, username):
        self.username = username
        self.data = None

    def fetch_data(self):
        headers = {
            "User-Agent": "CodingProfileScraper/1.0 (quitmanwakeley@gmail.com)",
        }
        url = f"https://www.hackerrank.com/rest/hackers/{self.username}/submission_histories"
        response = requests.get(url, headers=headers)
        self.data = response.json()

    def format_data(self):
        return self.data
