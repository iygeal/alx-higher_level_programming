#!/bin/bash
# Make a request to 0.0.0.0:5000/catch_me and check the response
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me >/dev/null 2>&1
