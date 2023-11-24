import pytest
import datetime
import json
from integrations.codechef import CodeChefScraper
from integrations.codeforces import CodeforcesScraper
from integrations.github import GitHubScraper
from integrations.hackerrank import HackerrankScraper
from integrations.kaggle import KaggleScraper
from integrations.leetcode import LeetCodeScraper


config_data = {
    "codechef": {"username": "quitty"},
    "codeforces": {"username": "quitty"},
    "github": {"username": "quitman-w"},
    "kaggle": {"username": "quitmanwakeley"},
    "leetcode": {"username": "quitty"},
    "hackerrank": {"username": "quitmanwakeley"},
}


@pytest.mark.parametrize(
    "scraper_class",
    [
        CodeChefScraper,
        CodeforcesScraper,
        GitHubScraper,
        HackerrankScraper,
        KaggleScraper,
        LeetCodeScraper,
    ],
)
def test_scraper(scraper_class):
    scraper_name = scraper_class.__name__.lower().replace("scraper", "")
    assert scraper_name in config_data
    # we should probably just pass in an object not username
    scraper = scraper_class(config_data[scraper_name]["username"])
    # Test init
    assert scraper is not None

    # Test fetching
    scraper.fetch_data()
    assert scraper.data is not None

    # Test formatting response
    formatted_data = scraper.format_data()
    for key, value in formatted_data.items():
        # should probably convert all these to datetime objects
        # Test response key is a string for date and value is an integer for count
        assert isinstance(key, str)
        assert isinstance(value, int)
