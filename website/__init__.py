# website/__init__.py
"""
makes the website folder into package, so the folder can be imported
"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    
    # Secure tracking signatures unique to your class section
    app.config['SECRET_KEY'] = 'BSCPE1-6_IskoGuide'
    
    # 🔐 FLASK SESSION LAYER FOR MEMORY APP REGISTRIES
    # Tells Flask to maintain user login roles safely inside server cookies
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_PERMANENT'] = False

    from .views import views
    from .auth import auth

    # Registering structural blueprints to map frontend paths cleanly
    app.register_blueprint(views, url_prefix='/')  
    app.register_blueprint(auth, url_prefix='/')

    return app