#!/usr/bin/python3
"""Python script that sends POST request and prints utf-8 response"""


from sys import argv
from urllib import request, parse

if __name__ == "__main__":

    my_url, email = argv[1], {'email': argv[2]}

    email = parse.urlencode(email).encode('utf-8')

    req = request.Request(my_url, data=email, method="POST")

    with request.urlopen(req) as response:
        page_body = response.read()
        decoded_page = page_body.decode('utf-8')
    print(decoded_page)
