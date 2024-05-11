#!/usr/bin/python3
"""Python script that fetches a URL using the requests package"""


import requests

url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)
print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
