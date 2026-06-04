import os
from flask import Flask

def create_app():
    # Locates the absolute path of the directory containing this __init__.py file
    base_dir = os.path.abspath(os.path.dirname(__file__))
    
    # Anchor template and static directories dynamically using absolute system pathways
    template_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')

    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.config['SECRET_KEY'] = 'iskoguide_encryption_token'

    # Register blueprints smoothly
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
    