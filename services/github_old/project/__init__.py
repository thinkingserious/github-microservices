import os
from flask import Flask

def create_app(script_info=None):
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # register blueprints
    from project.api.routes import routes_blueprint
    app.register_blueprint(routes_blueprint)

    @app.shell_context_processor
    def ctx():
        return {'app': app}
    
    return app
