import requests
from integrations.scraper_interface import Scraper
from dotenv import dotenv_values


class GitHubScraper(Scraper):
    github_url = "https://api.github.com/graphql"
    query = """
query($userName:String!) { 
  user(login: $userName){
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            contributionCount
            date
          }
        }
      }
    }
  }
}
"""

    def __init__(self, username):
        self.username = username
        self.token = dotenv_values()["GITHUB_TOKEN"]
        self.data = None

    def fetch_data(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        variables = {"userName": self.username}
        response = requests.post(
            GitHubScraper.github_url,
            headers=headers,
            json={"query": GitHubScraper.query, "variables": variables},
        )
        if response.status_code == 200:
            self.data = response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")

    def format_data(self):
        calendar_data = {}
        for week in self.data["data"]["user"]["contributionsCollection"][
            "contributionCalendar"
        ]["weeks"]:
            for day in week["contributionDays"]:
                if day["contributionCount"] > 0:
                    date = day["date"]
                    contribution_count = day["contributionCount"]
                    calendar_data[date] = contribution_count
        return calendar_data
