# website/__init__.py
import os
from flask import Flask

def create_app():
    """
    🏢 3-LAYER ARCHITECTURE - LAYER 1: PRESENTATION LAYER (APPLICATION FACTORY)
    This factory builds, configures, and initializes the Flask application context.
    It links the layout templates and registers presentation blueprints, serving as 
    the operational gateway for all incoming HTTP traffic.
    """
    # 🎯 FIX FOR OPTION 2: Locate the absolute path of the directory containing this __init__.py file
    base_dir = os.path.abspath(os.path.dirname(__file__))
    
    # Anchor template and static directories dynamically using absolute system pathways 
    # to completely eliminate path-mismatch crashes during automated unit tests.
    template_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')

    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    
    # Secure tracking signatures unique to your class section BSCPE 1-6
    app.config['SECRET_KEY'] = 'BSCPE1-6_IskoGuide'
    
    # 🔐 FLASK SESSION LAYER FOR MEMORY APP REGISTRIES
    # Tells Flask to maintain user login roles safely inside server cookies
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_PERMANENT'] = False

    from .views import views
    from .auth import auth

    # Registering structural blueprints to map frontend presentation paths cleanly
    app.register_blueprint(views, url_prefix='/')  
    app.register_blueprint(auth, url_prefix='/')

    return app
    