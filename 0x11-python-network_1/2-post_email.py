#~!/usr/bin/python3

"""
script takes in a url and email and sends a post request
"""
import sys
import urllib.request
from urllib.parse import urlencode


if __name__ == "__main__":
    url = sys.argv[1]
    mail = {"email": argv[2]}
    data = urlencode(mail).encode("ascii")
    url_request = urllib.request(url, data)
