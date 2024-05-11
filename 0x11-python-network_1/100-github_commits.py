#!/usr/bin/python3
"""10 commits (from the most recent to oldest) of the repository “rails”
    by the user “rails
”"""


from sys import argv
import requests

if __name__ == "__main__":
    repo, user = argv[1], argv[2]

    url = f"https://api.github.com/repos/{user}/{repo}/commits"

    # Send a GET request to the GitHub API endpoint
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()

        # Print the commits
        for commit in commits[:10]:  # Print the 10 most recent commits
            commit_hash = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{commit_hash}: {author_name}")
    else:
        print("Failed to retrieve commits. Status code:", response.status_code)
