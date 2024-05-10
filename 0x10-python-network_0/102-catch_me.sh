#!/bin/bash
# Make a request to 0.0.0.0:5000/catch_me and check the response
curl -s -X PUT -d "user_id=98" -L 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -H "Content-Length: 9" -d "You got me!"
