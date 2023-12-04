#!/usr/bin/python3

"""
script takes a url and sends it a request
"""

import sys
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = sys.argv[1]
    url_request = Request(url)

    with urlopen(url_request) as url_response:
        print(dict(url_response.headers).get("X-Request-Id"))
