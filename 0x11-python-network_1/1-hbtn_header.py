#!/usr/bin/python3

"""
script takes a url and sends it a request
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    url_request = urllib.request(url)

    with urlopen(url_request) as url_response:
        print(dict(url_response.headers).get("X-Request-Id"))
