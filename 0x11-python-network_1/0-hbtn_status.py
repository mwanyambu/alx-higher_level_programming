#!/usr/bin/python3

"""
script fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url_request = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(url_request) as url_response:
        body = url_response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
