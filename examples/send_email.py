from python_http_client import Client, exceptions
import os
import json
import time
import config

all_repos = config.REPOS

def send_email(from_email, to_email, subject, content):
    client = Client(host="http://{}".format(os.environ.get('GITHUB_MANAGER_MICROSERVICES_IP')))
    data = {
        "from_email": from_email,
        "to_email": to_email,
        "subject": subject,
        "content": content
    }
    response = client.email.post(request_body=data)

def get_prs(repo):
    client = Client(host="http://{}".format(os.environ.get('GITHUB_MANAGER_MICROSERVICES_IP')))
    repo_user, repo_name = repo.split("/")
    query_params = {
        "repo_user": repo_user,
        "repo_name": repo_name
    }
    response = client.github.prs.get(query_params=query_params)
    return json.loads(response.body)

total_prs_to_review = 0
for repo in all_repos:
    prs = get_prs(repo)
    for pr in prs:
        total_prs_to_review += 1

try:
    send_email(
        config.FROM_EMAIL,
        config.TO_EMAIL,
        'PRs! PRs everywhere!',
        'There are a total of {0} open prs needing a code review across all repos'.format(total_prs_to_review))
except Exception as e:
    print(e.body)
