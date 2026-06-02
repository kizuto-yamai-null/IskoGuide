# website/auth.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, make_response

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
            # 1: Admin, 2: Mod, 3: Student, 4: Visitor
            selected_role = int(request.form.get('role_choice', 4))

            # --- ROLE GATE: VISITOR (No credentials required) ---
            if selected_role == 4:
                session['role'] = 4
                session['user_email'] = "Guest_User"
                return redirect(url_for('views.home', role="Visitor"))

            # --- ROLE GATE: STUDENT (Uses Email & Password validation) ---
            elif selected_role == 3:
                # 🛠️ FIXED: Matched Dustin's frontend form name identifiers exactly
                email = request.form.get('email', '')
                password = request.form.get('password', '')

                # 🛠️ FIXED: Removed hasattr safetynet to call the direct verification engine
                if controller.verify_student(email, password):
                    session['role'] = 3
                    session['user_email'] = email
                    return redirect(url_for('views.home', role="Student"))
                else:
                    return render_template("login.html", error="Invalid Student credentials.")

            # --- ROLE GATE: STAFF (Admin / Moderator PIN Validation) ---
            else:
                user_pin = int(request.form.get('pin_input', 0))
                is_valid = controller.verify_credentials(
                    selected_role, user_pin)

                if is_valid:
                    role_label = "Admin" if selected_role == 1 else "Moderator"
                    session['role'] = selected_role
                    session['user_email'] = f"{role_label.lower()}@iskoguide.edu.ph"
                    return redirect(url_for('views.home', role=role_label))
                else:
                    return render_template("login.html", error="Invalid Security PIN. Access Denied.")

        except (ValueError, TypeError):
            return render_template("login.html", error="Invalid input format detected.")

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
    session.clear()  # Wipe session tokens cleanly
    return redirect(url_for('auth.login'))


# TRY ONLY

@auth.route('/auth', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        action = request.form.get('action')  # 'login' or 'signup'
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        # TODO: replace with your real auth logic
        if not username or not password:
            flash('Provide username and password', 'error')
            return redirect(request.path)

        if action == 'signup':
            # call your signup routine (e.g., create user in DB)
            flash(f'Signed up {username}', 'success')
        else:
            # call your login routine (verify password, create session)
            return f"<h>The account is Success</h>"

        return redirect(url_for('views.home'))  # adjust target after success

    # GET -> render a page (optional)
    return render_template('signup.html')
