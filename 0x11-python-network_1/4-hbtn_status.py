#!/usr/bin/python3

import requests
"""
script fetches a url
"""


if __name__ == "__main__":
    url_request = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(url_request.text)))
    print("\t- content: {}".format(url_request.text))
