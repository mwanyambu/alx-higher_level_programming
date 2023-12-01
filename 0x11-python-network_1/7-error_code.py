#!/usr/bin/python3

"""
script takes a url and sends it a request then it displays body of response
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    url_request = requests.get(url)

    if url_request.status_code >= 400:
        print("Error code: {}".format(url_request.status_code))
    else:
        print(url_request.text)
