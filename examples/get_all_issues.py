from python_http_client import Client
import os
import json
import time

all_repos = [
    'sendgrid/sendgrid-nodejs',
    'twilio/twilio-node'
]

def get_issues(repo):
    client = Client(host="http://{}".format(os.environ.get('GITHUB_MANAGER_MICROSERVICES_IP')))
    query_params = {
        "repo":repo
    }
    response = client.github.issues.get(query_params=query_params)
    return json.loads(response.body)

total_issues_to_review = 0
for repo in all_repos:
    issues = get_issues(repo)
    for issue in issues:
        print('{0}: {1} - {2}'.format(issue["number"], issue["title"], issue["url"]))
        total_issues_to_review += 1

print("There are a total of {} open issues needing a code review across all repos".format(total_issues_to_review))