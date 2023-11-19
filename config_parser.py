from integrations.codechef import CodeChefScraper
from integrations.codeforces import CodeforcesScraper
from integrations.github import GitHubScraper
from integrations.hackerrank import HackerrankScraper
from integrations.kaggle import KaggleScraper
from integrations.leetcode import LeetCodeScraper


class ConfigParser:
    def __init__(self, config):
        self.config = config
        self.scrapers = {
            "codechef": CodeChefScraper,
            "codeforces": CodeforcesScraper,
            "github": GitHubScraper,
            "hackerrank": HackerrankScraper,
            "kaggle": KaggleScraper,
            "leetcode": LeetCodeScraper,
        }
        self.data = {}

    def parse_configs(self):
        for key, value in self.config.items():
            if key.lower() in self.scrapers:
                scraper = self.scrapers[key](value["username"])
                scraper.fetch_data()
                self.data.update(scraper.format_data())
        return self.data


config_data = {
    "codechef": {"username": "quitty"},
    "codeforces": {"username": "quitty"},
    "github": {"username": "quitman-w"},
    "kaggle": {"username": "quitmanwakeley"},
    "leetcode": {"username": "quitty"},
    "hackerrank": {"username": "quitmanwakeley"},
}

config_parser = ConfigParser(config_data)
print(config_parser.parse_configs())
