# website/auth.py
from flask import Blueprint, render_template, request, redirect, url_prefix, url_for
from system_controller import IskoGuideController

auth = Blueprint('auth', __name__)

# Single shared initialization of your backend controller state
controller = IskoGuideController()

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Catches HTML login actions and runs validation rules using the backend controller.
    """
    if request.method == 'POST':
        # Retrieve input numbers from Versoza's HTML form inputs
        selected_role = int(request.form.get('role_choice'))
        user_pin = int(request.form.get('pin_input', 0))
        
        # Core logic gate verification check
        if selected_role == 3:  # Visitor path
            return redirect(url_for('views.home', role="Visitor"))
            
        is_valid = controller.verify_credentials(selected_role, user_pin)
        
        if is_valid:
            role_label = "Admin" if selected_role == 1 else "Moderator"
            return redirect(url_for('views.home', role=role_label))
        else:
            # Re-render login page with error text if PIN check fails
            return render_template("login.html", error="Invalid Security PIN. Access Denied.")
            
    return render_template("login.html", error=None)

@auth.route('/logout')
def logout():
    return redirect(url_for('auth.login'))

@auth.route('/signup')
def signup():
    return render_template("signup.html")