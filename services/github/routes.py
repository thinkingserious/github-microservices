import os
from flask import Blueprint, jsonify, current_app, request
from github import Github
routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/github/prs', methods=['GET'])
def get_prs():
    prs = []
    repo = request.args.get('repo', type=str)
    g = Github(current_app.config['GITHUB_TOKEN'])
    repo = g.get_repo(repo)
    pulls = repo.get_pulls(state='open', sort='created')
    for pr in pulls:
        prs.append({"number": pr.number,"url": pr.url, "title": pr.title})
    return jsonify(prs), 200

@routes_blueprint.route('/github/issues', methods=['GET'])
def get_issues():
    items = []
    repo = request.args.get('repo', type=str)
    g = Github(current_app.config['GITHUB_TOKEN'])
    repo = g.get_repo(repo)
    issues = repo.get_issues(state='open', sort='created')
    for issue in issues:
        items.append({"number": issue.number,"url": issue.url, "title": issue.title})
    return jsonify(items), 200
