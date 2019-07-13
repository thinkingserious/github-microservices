from python_http_client import Client
import os
import json
import time

all_repos = [
    'sendgrid/sendgrid-nodejs',
    'twilio/twilio-node'
]

def send_sms(from_number, to_number, body):
    client = Client(host="http://{}".format(os.environ.get('GITHUB_MANAGER_MICROSERVICES_IP')))
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

send_sms(
    '<A Phone Number Associated with your Account SID>  (e.g. +15551234444)',
    '<The destination Phone Number> (e.g. +15551234444)',
    'There are a total of {0} open prs needing a code review across all repos'.format(total_prs_to_review))
