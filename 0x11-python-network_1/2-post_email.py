#!/usr/bin/python3
""" Script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8). """


if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    from sys import argv

    url = argv[1]
    values = {
        'email': argv[2]
    }

    data = urlencode(values).encode('ascii')
    req = Request(url, data)

    with urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
