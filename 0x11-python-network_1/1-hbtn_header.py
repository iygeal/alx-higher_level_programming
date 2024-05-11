#!/usr/bin/python3
"""This python script takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response
"""


import sys
import urllib.request

if __name__ == "__main__":
    my_url = sys.argv[1]

    with urllib.request.urlopen(my_url) as response:
        response_headers = response.headers
        for key, value in response_headers.items():
            if key == "X-Request-Id":
                print(value)
