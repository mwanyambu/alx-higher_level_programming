#!/usr/bin/python3

"""
script takes in a url and email and sends a post request
"""
import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    mail = {'email': email}
    data = urlencode(mail).encode('ascii')
    request = Request(url, data=data, method='Post')

    with urlopen(request) as response:
        print(response.read().decode('utf-8'))
