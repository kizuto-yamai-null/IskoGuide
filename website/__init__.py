"""
makes the website folder into package, so the folder can be imported
"""

from flask import Flask, session


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'BSCPE1-6_IskoGuide'

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

    app.register_blueprint(views, url_prefix='/')  # Registering blueprint
    app.register_blueprint(auth, url_prefix='/')

    return app
