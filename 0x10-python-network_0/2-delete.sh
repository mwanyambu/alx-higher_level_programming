#!/usr/bin/bash
#script sends a delete request to a url passed as first argument
curl -sX DELETE "$1"
