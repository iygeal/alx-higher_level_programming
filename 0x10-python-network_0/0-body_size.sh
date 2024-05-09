#!/bin/bash
# This script takes in a URL as an argument, sends a request to that URL using curl, and displays the size of the body of the response in bytes
curl -s -w "%{size_download}" -o /dev/null "$1"
