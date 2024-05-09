ALX AFRICA! 0x10. Python - Network #0
===

General Objectives for the Project
---
What a URL is
What HTTP is
How to read a URL
The scheme for a HTTP URL
What a domain name is
What a sub-domain is
How to define a port number in a URL
What a query string is
What an HTTP request is
What an HTTP response is
What HTTP headers are
What the HTTP message body is
What an HTTP request method is
What an HTTP response status code is
What an HTTP Cookie is
How to make a request with cURL
What happens when you type google.com in your browser (Application level)


Task 0:
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

IMPLEMENTATION
===

#!/bin/bash
# This script takes in a URL as an argument, sends a request to that URL using curl,
# and displays the size of the body of the response in bytes

# curl: command-line tool for transferring data with URLs
# -s: Silent mode, suppresses progress meter and other output
# -w "%{size_download}": Specifies a custom output format to print the size of the downloaded content
# -o /dev/null: Redirects the output of the download to /dev/null, discarding the downloaded content
# "$1": The URL provided as the first argument to the script, to which the request is sent
curl -s -w "%{size_download}" -o /dev/null "$1"
