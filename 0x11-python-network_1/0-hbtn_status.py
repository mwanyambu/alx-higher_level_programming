#!/usr/bin/python3

import urllib.request
"""
script fetches a url
"""


if __name__ == "__main__":
    url_request = urllib.request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(url_request) as url_response:
        body = url_response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
