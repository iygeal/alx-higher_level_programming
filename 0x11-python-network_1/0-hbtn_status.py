#!/usr/bin/python3
"""Python script that fetches a url"""


import urllib.request

if __name__ == "__main__":
    my_site = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(my_site) as response:
        page_body = response.read()

        page_decoded = page_body.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(page_body))
    print("\t- content:", page_body)
    print("\t- utf8 content:", page_decoded)
