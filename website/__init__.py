# website/__init__.py
import os
from flask import Flask, session

def create_app():
    """
    🏢 3-LAYER ARCHITECTURE - LAYER 1: PRESENTATION LAYER (APPLICATION FACTORY)
    This factory builds, configures, and initializes the Flask application context.
    It links the layout templates and registers presentation blueprints, serving as 
    the operational gateway for all incoming HTTP traffic.
    """
    # Locate the absolute path of the directory containing this __init__.py file
    base_dir = os.path.abspath(os.path.dirname(__file__))
    
    # Anchor the absolute folder paths for templates and static assets
    template_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')

    # Initialize Flask by forcing it to strictly look at the absolute template directory
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    
    # Secure tracking signatures unique to your class section BSCPE 1-6
    app.config['SECRET_KEY'] = 'BSCPE1-6_IskoGuide'
    
    # 🔐 FLASK SESSION LAYER FOR MEMORY APP REGISTRIES
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_PERMANENT'] = False

    # 🎭 DYNAMIC ROLE CONTEXT INJECTION (Dustin's Feature Integration)
    @app.context_processor
    def inject_user_context():
        role_num = session.get('role', 4)
        role_labels = {1: "Admin", 2: "Moderator", 3: "Student", 4: "Visitor"}
        return {
            "current_role": role_num,
            "current_role_label": role_labels.get(role_num, "Visitor"),
            "current_user_email": session.get("user_email", "Guest_User"),
        }

    from .views import views
    from .auth import auth

    # Registering structural blueprints to map frontend presentation paths cleanly
    app.register_blueprint(views, url_prefix='/')  
    app.register_blueprint(auth, url_prefix='/')

    return app
