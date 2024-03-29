#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response. """


if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from sys import argv

    url = argv[1]
    req = Request(url)

    with urlopen(req) as response:
        header = response.headers
        print(header['X-Request-Id'])
