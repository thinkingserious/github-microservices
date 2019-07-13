import os

class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    TWILIO_ACCOUNT_SID=os.environ['TWILIO_ACCOUNT_SID']
    TWILIO_AUTH_TOKEN=os.environ['TWILIO_AUTH_TOKEN']

