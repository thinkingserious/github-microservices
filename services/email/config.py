import os

class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SENDGRID_API_KEY=os.environ['SENDGRID_API_KEY']
