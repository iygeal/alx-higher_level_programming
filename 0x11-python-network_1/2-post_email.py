#!/usr/bin/python3
"""Python script that sends POST request and prints utf-8 response"""


from sys import argv
import urllib.request

if __name__ == "__main__":

    my_url, email = argv[1], {'email': argv[2]}

    email = email.encode('utf-8')

    req = urllib.request.Request(my_url, email)

    with urllib.request.urlopen(req) as response:
        page_body = response.read()
        decoded_page = page_body.decode('utf-8')
    print(decoded_page)
