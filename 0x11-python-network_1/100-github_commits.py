#!/usr/bin/python3
""" Script that lists 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”. """


if __name__ == "__main__":
    import requests
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    api_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    commits = 10
    params = {'per_page': commits}

    response = requests.get(api_url, params=params)
    response = response.json()

    for commit in response:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
