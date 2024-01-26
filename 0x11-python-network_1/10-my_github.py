#!/usr/bin/python3
""" Script that takes GitHub credentials (username and password) and uses the
GitHub API to display user id. """


if __name__ == "__main__":
    import requests
    from sys import argv

    api_url = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]
    auth = (username, password)

    r = requests.get(api_url, auth=auth)

    if r.status_code == 200:
        json_r = r.json()
        user_id = json_r.get('id')
        print(user_id)
    else:
        print("None")
