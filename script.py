import requests
import os
import re


github_token = os.environ["GITHUB_TOKEN"]
repo_name = os.environ["REPO_NAME"]
head_branch = os.environ["HEAD_BRANCH"]


def get_version_number(last_merge_pr):
    float_match = re.search(r'\d+(\.\d+)?', last_merge_pr["title"])
    if float_match:
        float_value = float(float_match.group())
        return float_value + 0.01
    return 1.99


all_pr = requests.get(
    f'https://api.github.com/repos/altooro/{repo_name}/pulls?state=closed&sort=created&direction=desc&per_page=50',
    headers={'Authorization': f'token {github_token}'}
).json()

last_production_pr = {}
pr_number_to_merge = []
for pr in all_pr:
    if pr["base"]["ref"] == 'production':
        last_production_pr = pr
        break
    if pr["merged_at"] and pr["base"]["ref"] == head_branch:
        pr_number_to_merge.append(pr["number"])

if pr_number_to_merge and last_production_pr:
    version_title = f"V {get_version_number(last_production_pr)}"
    body = '\n'.join([f'- #{pr}' for pr in pr_number_to_merge])
    url = f'https://api.github.com/repos/altooro/{repo_name}/pulls'
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'title': version_title,
        'body': body,
        'head': head_branch,
        'base': "production"
    }
    requests.post(url, json=data, headers=headers)
