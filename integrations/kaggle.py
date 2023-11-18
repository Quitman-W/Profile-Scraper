import requests

preliminary_url = "https://www.kaggle.com/alexisbcook"
preliminary_response = requests.get(preliminary_url)

generated_cookie = preliminary_response.cookies.get_dict()
main_url = "https://www.kaggle.com/api/i/users.ProfileService/GetUserActivity"
headers = {
    "X-Xsrf-Token": generated_cookie["XSRF-TOKEN"],
    "Cookie": "; ".join([f"{key}={value}" for key, value in generated_cookie.items()]),
}

response = requests.post(
    main_url,
    headers=headers,
    data='{"userName": "alexisbcook"}',
)
"""
data = {
    "activities": [
        {
            "date": "2023-01-25T00:00:00Z",
            "totalScriptsCount": 1,
            "totalDiscussionsCount": 3,
        },
        {"date": "2023-02-13T00:00:00Z", "totalScriptsCount": 4},
        {
            "date": "2023-03-29T00:00:00Z",
            "totalScriptsCount": 1,
            "totalDiscussionsCount": 1,
        },
        {"date": "2023-04-14T00:00:00Z", "totalScriptsCount": 4},
        {"date": "2023-04-18T00:00:00Z", "totalScriptsCount": 14},
        {"date": "2023-04-20T00:00:00Z", "totalScriptsCount": 69},
        {"date": "2023-04-21T00:00:00Z", "totalScriptsCount": 18},
        {"date": "2023-06-30T00:00:00Z", "totalScriptsCount": 1},
        {"date": "2023-01-24T00:00:00Z", "totalDiscussionsCount": 8},
        {"date": "2023-01-26T00:00:00Z", "totalDiscussionsCount": 2},
        {"date": "2023-01-27T00:00:00Z", "totalDiscussionsCount": 1},
        {"date": "2023-02-01T00:00:00Z", "totalDiscussionsCount": 1},
        {"date": "2023-02-02T00:00:00Z", "totalDiscussionsCount": 4},
        {"date": "2023-02-15T00:00:00Z", "totalDiscussionsCount": 1},
        {"date": "2023-02-16T00:00:00Z", "totalDiscussionsCount": 1},
        {"date": "2023-02-17T00:00:00Z", "totalDiscussionsCount": 1},
        {"date": "2023-02-21T00:00:00Z", "totalDiscussionsCount": 2},
        {"date": "2023-02-23T00:00:00Z", "totalDiscussionsCount": 1},
        {"date": "2023-03-03T00:00:00Z", "totalDiscussionsCount": 3},
        {"date": "2023-03-06T00:00:00Z", "totalDiscussionsCount": 1},
        {"date": "2023-04-10T00:00:00Z", "totalDiscussionsCount": 1},
        {"date": "2023-05-23T00:00:00Z", "totalDiscussionsCount": 2},
    ]
}
"""
print(response.json())
