import requests

url = "https://www.hackerrank.com/rest/hackers/quitmanwakeley/submission_histories"

headers = {
    "User-Agent": "CodingProfileScraper/1.0 (quitmanwakeley@gmail.com)",
}

response = requests.get(url, headers=headers)

print(response.json())
