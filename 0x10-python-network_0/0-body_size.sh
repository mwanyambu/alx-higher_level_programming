#!/bin/bash
#script takes an url and sends a request to it and returns its size
curl -sI "$1" | grep Content-Length: | cut -d " " -f 2
