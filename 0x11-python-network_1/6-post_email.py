#!/usr/bin/python3
"""This script takes in a URL and an email
    address, sends a POST request to the passed URL
    with the email as a parameter and displays the body of the response
"""


from sys import argv
import requests

if __name__ == "__main__":
    url, email = argv[1], {'email': argv[2]}
    response = requests.post(url, data=email)
    print(response.text)
