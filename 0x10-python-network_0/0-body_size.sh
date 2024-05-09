#!/bin/bash
# This script takes in a URL as an argument, sends a request to that URL using curl,
# and displays the size of the body of the response in bytes

# curl: command-line tool for transferring data with URLs
# -s: Silent mode, suppresses progress meter and other output
# -w "%{size_download}": Specifies a custom output format to print the size of the downloaded content
# -o /dev/null: Redirects the output of the download to /dev/null, discarding the downloaded content
# "$1": The URL provided as the first argument to the script, to which the request is sent
curl -s -w "%{size_download}" -o /dev/null "$1"
