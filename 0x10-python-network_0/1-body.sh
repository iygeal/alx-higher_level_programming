#!/bin/bash
# Send a GET request to the URL and display the body of the response
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q "200" && curl -s "$1"
