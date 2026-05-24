"""
makes the website folder into package, so the folder can be imported
"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'BSCPE1-6_IskoGuide'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')  # Registering blueprint
    app.register_blueprint(auth, url_prefix='/')

    return app
