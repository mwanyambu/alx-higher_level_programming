#~!/usr/bin/python3

"""
script takes in a url and email and sends a post request
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    mail = {"email": argv[2]}
    url_request = requests.post(url, data=mail)

    print(url_request.text)
