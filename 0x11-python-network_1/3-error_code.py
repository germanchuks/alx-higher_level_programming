#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8). """


if __name__ == "__main__":
    from urllib.request import Request, urlopen, HTTPError
    from urllib.parse import urlencode
    from sys import argv

    url = argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)

    except HTTPError as err:
        print(f"Error code: {err.code}")
