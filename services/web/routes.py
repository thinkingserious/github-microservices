import os
import json
from flask import Blueprint, jsonify, current_app, request, render_template
from python_http_client import Client
routes_blueprint = Blueprint('routes', __name__)

def get_issues(repo):
    client = Client(host="http://{}".format(os.environ.get('GITHUB_MANAGER_MICROSERVICES_IP')))
    query_params = {
        "repo":repo
    }
    response = client.github.issues.get(query_params=query_params)
    return json.loads(response.body)

def get_prs(repo):
    client = Client(host="http://{}".format(os.environ.get('GITHUB_MANAGER_MICROSERVICES_IP')))
    query_params = {
        "repo":repo
    }
    response = client.github.prs.get(query_params=query_params)
    return json.loads(response.body)

@routes_blueprint.route('/', methods=['GET'])
def dashboard():
    all_repos = [
        'sendgrid/sendgrid-nodejs',
        'twilio/twilio-node'
    ]
    
    total_issues_to_review = 0
    for repo in all_repos:
        issues = get_issues(repo)
        for issue in issues:
            print('{0}: {1} - {2}'.format(issue["number"], issue["title"], issue["url"]))
            total_issues_to_review += 1
    
    total_prs_to_review = 0
    for repo in all_repos:
        prs = get_prs(repo)
        for pr in prs:
            print('{0}: {1} - {2}'.format(pr['number'], pr['title'], pr['url']))
            total_prs_to_review += 1

    return render_template('index.html', title='Dashboard', num_prs=total_prs_to_review, num_issues=total_issues_to_review)

@routes_blueprint.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!',
        'container_id': os.uname()[1]
    }), 200
