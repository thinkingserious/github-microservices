from python_http_client import Client
import os
import json
import time
import config

all_repos = config.REPOS

def send_sms(from_number, to_number, body):
    client = Client(host="http://{}".format('hello.world'))
    data = {
        "from_number": from_number,
        "to_number": to_number,
        "body": body
    }
    response = client.sms.post(request_body=data)

def get_prs(repo):
    client = Client(host="http://{}".format(os.environ.get('GITHUB_MANAGER_MICROSERVICES_IP')))
    query_params = {
        "repo":repo
    }
    response = client.github.prs.get(query_params=query_params)
    return json.loads(response.body)

total_prs_to_review = 0
for repo in all_repos:
    prs = get_prs(repo)
    for pr in prs:
        total_prs_to_review += 1

try:
    send_sms(
        config.FROM_PHONE_NUMBER,
        config.TO_PHONE_NUMBER,
        'There are a total of {0} open prs needing a code review across all repos'.format(total_prs_to_review))
except Exception as e:
    print(e.body)

