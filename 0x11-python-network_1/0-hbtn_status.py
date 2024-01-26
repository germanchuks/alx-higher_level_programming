#!/usr/bin/python3
"""Script that fetches `https://alx-intranet.hbtn.io/status`"""


if __name__ == "__main__":
    from urllib.request import Request, urlopen

    url = 'https://alx-intranet.hbtn.io/status'
    req = Request(url)

    with urlopen(req) as response:
        body = response.read()
        decoded_content = body.decode('utf-8')
        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {decoded_content}")
