import os
from flask import Blueprint, jsonify, current_app, request
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/email', methods=['POST'])
def send_email():
    r = request.get_json()
    message = Mail(
        from_email=r['from_email'],
        to_emails=r['to_email'],
        subject=r['subject'],
        html_content=r['content'])
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    return jsonify([{"message": "success"}]), 200

@routes_blueprint.route('/email/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!',
        'container_id': os.uname()[1]
    }), 200