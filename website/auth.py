# website/auth.py
from flask import Blueprint, render_template, request, redirect, url_for, session

# Corrected to absolute root import to find the file in the main IskoGuide folder
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
        try:
            # 1. Read the form elements Dustin is providing
            try:
                selected_role = int(request.form.get('role_choice', 4))
            except (ValueError, TypeError):
                selected_role = 4 # Fallback safely to Visitor access
            
            # --- ROLE GATE: VISITOR (No credentials required) ---
            if selected_role == 4:  
                session['role'] = 4
                session['user_email'] = "Guest_User"
                return redirect(url_for('views.home', role="Visitor"))
                
            # --- ROLE GATE: STUDENT (Uses Email & Password validation) ---
            elif selected_role == 3:
                email = request.form.get('email', '')
                password = request.form.get('password', '')
                
                if controller.verify_student(email, password):
                    session['role'] = 3
                    session['user_email'] = email
                    return redirect(url_for('views.home', role="Student"))
                else:
                    return render_template("login.html", error="Invalid Student credentials.")

            # --- ROLE GATE: STAFF (Admin / Moderator PIN Validation) ---
            else:
                # 🛡️ DEFENSIVE GUARD: Catch non-numeric PIN strings safely inside the execution logic
                try:
                    user_pin = int(request.form.get('pin_input', 0))
                except (ValueError, TypeError):
                    return render_template("login.html", error="Invalid Security PIN. Access Denied (Numeric inputs only).")

                is_valid = controller.verify_credentials(selected_role, user_pin)
                
                if is_valid:
                    role_label = "Admin" if selected_role == 1 else "Moderator"
                    session['role'] = selected_role
                    session['user_email'] = f"{role_label.lower()}@iskoguide.edu.ph"
                    return redirect(url_for('views.home', role=role_label))
                else:
                    return render_template("login.html", error="Invalid Security PIN. Access Denied.")
                    
        except Exception as e:
            # Universal catch-all shield to keep the interface functional no matter what data lands
            return render_template("login.html", error="An unexpected system error occurred.")
            
    return render_template("login.html", error=None)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Handles capturing input from Dustin's signup form and sending it to the controller.
    """
    if request.method == 'POST':
        # 🛠️ FIXED: Matched Dustin's frontend registration fields
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        
        # 🛠️ FIXED: Removed hasattr check to directly register the student object instance
        success, message = controller.register_student(email, password)
        if success:
            return redirect(url_for('auth.login'))
        return render_template("signup.html", error=message)
            
    return render_template("signup.html", error=None)


@auth.route('/logout')
def logout():
    session.clear() # Wipe session tokens cleanly
    return redirect(url_for('auth.login'))