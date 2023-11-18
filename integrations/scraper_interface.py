from abc import ABC, abstractmethod


class Scraper(ABC):
    @abstractmethod
    def __init__(self, username):
        pass

    @abstractmethod
    def fetch_data(self):
        pass

    @abstractmethod
    def format_data(self):
        pass
