#!/bin/bash
# Make a request to 0.0.0.0:5000/catch_me and check the response
curl -s http://0.0.0.0:5000/catch_me | grep -q "You got me!" && echo "You got me!"
