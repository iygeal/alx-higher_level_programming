#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""


from sys import argv
import requests

if __name__ == "__main__":
    username, password = argv[1], argv[2]

    url = "https://api.github.com/user"

    auth = (username, password)

    response = requests.get(url, data=auth)

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data['id']
        print("Your GitHub id is:", user_id)
    else:
        print("Failed to retrieve id. Status code:", response.status_code)
