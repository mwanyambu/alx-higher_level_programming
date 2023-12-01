#!/usr/bin/python3

"""
script takes a url and sends it a request then it displays body of response
"""

import sys
from urllib.error import HTTPError
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    url_request = urllib.request(url)

    try:
        with urllib.request.urlopen(url_request) as response:
            print(response.read().decode("ascii"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
