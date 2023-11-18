import requests
from scraper_interface import Scraper
import json

# probably going to swap this to kaggles internal api instead of this for more features


class KaggleScraper(Scraper):
    def __init__(self, username):
        self.username = username
        self.data = None

    # necessary to grab cookie first
    def fetch_data(self):
        preliminary_url = f"https://www.kaggle.com/{self.username}"
        preliminary_response = requests.get(preliminary_url)

        generated_cookie = preliminary_response.cookies.get_dict()
        main_url = "https://www.kaggle.com/api/i/users.ProfileService/GetUserActivity"
        headers = {
            "X-Xsrf-Token": generated_cookie["XSRF-TOKEN"],
            "Cookie": "; ".join(
                [f"{key}={value}" for key, value in generated_cookie.items()]
            ),
        }

        # need to stringify payload
        response = requests.post(
            main_url,
            headers=headers,
            data=json.dumps({"userName": self.username}),
        )
        self.data = response.json()
        return self.data

    def format_data(self):
        calendar_data = {}
        for data in self.data["activities"]:
            formatted_date = data["date"][0:10]
            submissions = 0
            # multiple different types of submission on kaggle
            for key, value in data.items():
                if key != "date":
                    submissions += value
            calendar_data[formatted_date] = submissions
        return calendar_data
