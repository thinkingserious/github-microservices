import os
from flask import Blueprint, jsonify, current_app, request
from twilio.rest import Client
routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/sms', methods=['POST'])
def send_sms():
    r = request.get_json()
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    try:
        message = client.messages \
                        .create(
                            body=r['body'],
                            from_=r['from_number'],
                            to=r['to_number']
                        )
    except Exception as e:
        return jsonify([{"message": str(e)}]), 500
    return jsonify([{"message": "success"}]), 200
