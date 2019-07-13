from python_http_client import Client, exceptions
import os
import json
import time

all_repos = [
    'sendgrid/sendgrid-nodejs',
    'twilio/twilio-node'
]

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

send_email(
    '<From email> (e.g. dx@sendgrid.com)',
    '<Destination email> (e.g. ethomas@twilio.com)',
    'PRs! PRs everywhere!',
    'There are a total of {0} open prs needing a code review across all repos'.format(total_prs_to_review))
