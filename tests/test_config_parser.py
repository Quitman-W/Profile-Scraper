from config_parser import ConfigParser
from integrations.codechef import CodeChefScraper
import pytest

config_data = {
    "codechef": {"username": "quitty"},
    "codeforces": {"username": "quitty"},
    "github": {"username": "quitman-w"},
    "kaggle": {"username": "quitmanwakeley"},
    "leetcode": {"username": "quitty"},
    "hackerrank": {"username": "quitmanwakeley"},
}


def test_parse_config_valid_key():
    data = {"hackerrank": {"username": "quitmanwakeley"}}
    config_parser = ConfigParser(data)
    result = config_parser.parse_configs()
    assert len(result) >= 1


def test_parse_config_invalid_key(capsys):
    config_data = {"🚀": {"username": "🚀"}}
    config_parser = ConfigParser(config_data)
    config_parser.parse_configs()
    captured = capsys.readouterr()
    assert "🚀 is not a valid scraping option." in captured.out


def test_parse_config_exception_error(capsys):
    config_data = {"leetcode": {"username": "🚀"}}
    config_parser = ConfigParser(config_data)
    config_parser.parse_configs()
    captured = capsys.readouterr()
    assert (
        "Unexpected error for leetcode: 'NoneType' object is not subscriptable"
        in captured.out
    )
