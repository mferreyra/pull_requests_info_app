
import os
import requests

TOKEN = os.getenv("TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}"}
PER_PAGE = 100

TOKEN = os.getenv("TOKEN")
HEADERS = {'Authorization': f'Bearer {TOKEN}'}


def get_pull_requests(state):
    """
    Example of return:
    [
        {"title": "Add useful stuff", "num": 56, "link": "https://github.com/boto/boto3/pull/56"},
        {"title": "Fix something", "num": 57, "link": "https://github.com/boto/boto3/pull/57"},
    ]
    """

    URL = f"https://api.github.com/repos/boto/boto3/pulls?state={state}&per_page={PER_PAGE}"
    print(URL)
    response = requests.get(url=URL, headers=HEADERS)

    data = response.json()
    pull_requests = []

    for pull in data:
        pull_requests.append(
            {"title": pull["title"], "num": pull["number"], "link": pull["html_url"]}
        )

    return pull_requests
