#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
    to a URL with the letter as a parameter
"""


from sys import argv
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        letter = argv[1]
    else:
        letter = ""

    data = {'q': letter}
    response = requests.post(url, data=data)

    try:
        json_response = response.json()
        if json_response:
            print(f"[{json_response['id']}] {json_response['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
