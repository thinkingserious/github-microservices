import os
from flask import Flask
from config import BaseConfig

app = Flask(__name__)

# set config
app.config.from_object(BaseConfig)

# register blueprints
from routes import routes_blueprint
app.register_blueprint(routes_blueprint)

if __name__ == '__main__':
    app.run()
