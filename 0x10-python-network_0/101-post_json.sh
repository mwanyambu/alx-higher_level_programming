#!/usr/bin/bash
#script sends post request to url as first arg
curl -sX --data @"$2" --header "Content-type: application/json" "$1"
