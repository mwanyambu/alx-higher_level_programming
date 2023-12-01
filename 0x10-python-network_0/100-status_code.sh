#!/bin/bash
#script sends a request to url and returns status code
curl -sX HEAD -w "%{http_code}""$1"
