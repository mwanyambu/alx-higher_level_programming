#!/usr/bin/bash
#script takes a url as argument and distplays all methods accepted byu server
curl -sI "$1" | grep Allow | cut -d " " -f 2-
