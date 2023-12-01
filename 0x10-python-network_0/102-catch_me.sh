#!/bin/bash
# script makes a reuests to 0.0.0.0:5000
curl -sLX PUT --data "user_id=98" --header "origin:HolbertonSchool" 0.0.0.0:5000/catch_me
