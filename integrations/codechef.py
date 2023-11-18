import json
import requests
import re
from scraper_interface import Scraper


class CodeChefScraper(Scraper):
    codechef_url = "https://www.codechef.com/users/"

    def __init__(self, username):
        self.username = username
        self.data = None

    def fetch_data(self):
        try:
            response = requests.get(f"{CodeChefScraper.codechef_url}{self.username}")
            response.raise_for_status()
            self.data = response.text
        except Exception as e:
            print(f"Error fetching data for {self.username}: {e}")

    # regex to parse out user submissions
    # looks like data is embedded in html so this or soup
    def extract_data(self):
        pattern = re.compile(r"var userDailySubmissionsStats = (.*?);")
        matches = pattern.findall(self.data)
        return json.loads(matches[0]) if matches else None

    def format_data(self):
        submission_data = self.extract_data()

        if submission_data:
            date_dict = {}
            for value in submission_data:
                date_dict[value["date"]] = value["value"]
            return date_dict
        else:
            print(f"Script content not found for {self.username}")
