#!/usr/bin/python3
"""This scripts takes in a URL, sends a request to it
    and displays the body of the response, raises exception too
"""


from sys import argv
from urllib import error, request

if __name__ == "__main__":
    my_url = argv[1]
    try:
        with request.urlopen(my_url) as response:
            page_body = response.read()
            decoded_body = page_body.decode('utf-8')
            print(decoded_body)
    except error.HTTPError as e:
        print("Error code:", e)
