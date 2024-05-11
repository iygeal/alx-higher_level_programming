#!/usr/bin/python3
"""This python script takes in a URL, sends a request to it
    and  displays the value of X-Request-Id variable
"""


from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)

    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
