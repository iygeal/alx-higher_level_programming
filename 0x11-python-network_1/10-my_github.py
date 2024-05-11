#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""


from sys import argv
import sys
import requests

if __name__ == "__main__":
    try:
        username, password = argv[1], argv[2]

        url = "https://api.github.com/user"

        auth = (username, password)

        response = requests.get(url, auth=auth)

        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data['id']
            print(user_id)
        else:
            print("Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("GitHub API inaccessible: code", e)
        sys.exit(1)
