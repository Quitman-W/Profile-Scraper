import requests
import json
import datetime


def convert_timestamp_to_date(timestamp):
    return datetime.datetime.utcfromtimestamp(int(timestamp)).strftime("%Y-%m-%d")


def extract_dates(data):
    if isinstance(data, dict):
        return {
            convert_timestamp_to_date(key): extract_dates(value)
            for key, value in data.items()
        }
    elif isinstance(data, list):
        return [extract_dates(item) for item in data]
    else:
        return data


graphql_query = """
    query userProfileCalendar($username: String!, $year: Int) {
      matchedUser(username: $username) {
        userCalendar(year: $year) {
          submissionCalendar
        }
      }
    }
"""

variables = {"username": "Quitty"}

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

calendar_data = extract_dates(
    json.loads(response["data"]["matchedUser"]["userCalendar"]["submissionCalendar"])
)

for date, value in calendar_data.items():
    print(date, value)
