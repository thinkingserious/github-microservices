import os
from flask import Blueprint, jsonify, current_app, request
from github3 import login
routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/github/prs', methods=['GET'])
def get_prs():
    prs = []
    repo_user = request.args.get('repo_user', type=str)
    repo_name = request.args.get('repo_name', type=str)
    g = login(token=current_app.config['GITHUB_TOKEN'])
    repo = g.repository(repo_user, repo_name)
    pulls = repo.iter_pulls(state='open', base='master')
    for pr in pulls:
        prs.append({"number": pr.number,"url": pr.html_url, "title": pr.title})
    return jsonify(prs), 200

@routes_blueprint.route('/github/issues', methods=['GET'])
def get_issues():
    items = []
    repo_user = request.args.get('repo_user', type=str)
    repo_name = request.args.get('repo_name', type=str)
    g = login(token=current_app.config['GITHUB_TOKEN'])
    repo = g.repository(repo_user, repo_name)
    issues = repo.iter_issues(state='open')
    for issue in issues:
        items.append({"number": issue.number,"url": issue.html_url, "title": issue.title})
    return jsonify(items), 200

@routes_blueprint.route('/github/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!',
        'container_id': os.uname()[1]
    }), 200