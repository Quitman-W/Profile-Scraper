import requests
import datetime
import json
from integrations.scraper_interface import Scraper


class LeetCodeScraper(Scraper):
    def __init__(self, username):
        self.username = username
        self.data = None

    def fetch_data(self):
        graphql_query = """
            query userProfileCalendar($username: String!, $year: Int) {
              matchedUser(username: $username) {
                userCalendar(year: $year) {
                  submissionCalendar
                }
              }
            }
        """

        variables = {"username": self.username}

        operation_name = "userProfileCalendar"

        graphql_endpoint = "https://leetcode.com/graphql/"

        headers = {
            "Content-Type": "application/json",
        }

        payload = {
            "query": graphql_query,
            "variables": variables,
            "operationName": operation_name,
        }

        response = requests.post(graphql_endpoint, json=payload, headers=headers).json()
        self.data = json.loads(
            response["data"]["matchedUser"]["userCalendar"]["submissionCalendar"]
        )

    def format_data(self):
        calendar_data = {}
        for key, value in self.data.items():
            date = self.convert_timestamp_to_date(int(key))
            calendar_data[date] = value
        return calendar_data

    def convert_timestamp_to_date(self, timestamp):
        return datetime.datetime.utcfromtimestamp(int(timestamp)).strftime("%Y-%m-%d")
