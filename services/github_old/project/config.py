import os

class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    GITHUB_TOKEN=os.environ.get('GITHUB_TOKEN')
