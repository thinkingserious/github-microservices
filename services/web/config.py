import os

class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    GITHUB_MANAGER_MICROSERVICES_IP=os.environ['GITHUB_MANAGER_MICROSERVICES_IP']
