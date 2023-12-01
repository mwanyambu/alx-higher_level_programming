#!/usr/bin/python3

"""
script takes a url and sends it a request
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    url_request = requests.get(url)

    print(url_response.headers.get("X-Request-Id"))
