import re
import json
import requests
from integrations.scraper_interface import Scraper


class CodeforcesScraper(Scraper):
    codeforces_url = "https://codeforces.com/profile/"

    def __init__(self, username):
        self.username = username
        self.data = None

    def fetch_data(self):
        response = requests.get(f"{CodeforcesScraper.codeforces_url}{self.username}")
        self.data = response.text

    # regex to parse out user submissions
    # looks like data is embedded in html so this or soup
    def extract_data(self):
        pattern = re.compile(r"data:\s*({[\s\S]*?}),\s*start_monday:")
        matches = pattern.findall(self.data)
        if matches:
            self.data = json.loads(matches[0].strip().replace("items", '"items"'))
        else:
            print("Data not found.")

    def format_data(self):
        self.extract_data()
        calendar_data = {}
        # codeforces "submissions aren't individual submissions but activity ranking from 1-5
        for key, value in self.data.items():
            calendar_data[key] = value["items"][0]
        return calendar_data
