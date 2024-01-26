#!/usr/bin/python3
""" Script  that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter. """


if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    letter = "" if len(argv) == 0 else argv[1]
    payload = {
        'q': letter
    }

    r = requests.post(url, data=payload)
    try:
        json_r = r.json()
        if json_r:
            print(f"[{json_r.get("id")}] {json_r.get("name")}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
