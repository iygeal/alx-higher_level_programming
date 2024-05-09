#!/bin/bash
# Send a GET request to the URL and display the body of the response
[[ "$(curl -so /dev/null -w "%{http_code}" "$1")" -eq 200 ]] && curl -s "$1"

