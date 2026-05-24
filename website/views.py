# website/views.py
from flask import Blueprint, render_template, request
from website.auth import controller  # Import the single shared controller instance

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home():
    # Detect active role string passed from authentication page state
    current_role = request.args.get('role', 'Visitor')
    return render_template("home.html", role=current_role)

@views.route('/admission')
def admission_guide():
    """
    Fetches raw requirements data arrays directly out of the data files 
    via the admission module instance.
    """
    guide_data = controller.admission_module.get_Enrollment_Steps()
    return render_template("admission.html", data=guide_data)

@views.route('/scholarship', methods=['GET', 'POST'])
def scholarship_checker():
    """
    Receives GWA decimal inputs from browser forms and runs evaluation rules.
    """
    result_message = None
    if request.method == 'POST':
        student_gwa = float(request.form.get('gwa'))
        # Execute logic inside your module instance
        result_message = controller.scholarship_module.check_Eligibility(student_gwa)
        
    return render_template("scholarship.html", feedback=result_message)