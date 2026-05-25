# website/views.py
from flask import Blueprint, render_template, request
# Import the structural skeleton classes you just created
from modules.admission import AdmissionModule
from modules.scholarship import ScholarshipModule

views = Blueprint('views', __name__)

# Instantiate the modules so they are ready to process data
admission_engine = AdmissionModule()
scholarship_engine = ScholarshipModule()

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/admission')
def admission_guide():
    # Fetch the structural data from your module layer
    steps = admission_engine.show_Enrollment_Guide()
    # Pass it straight into Versoza's HTML frontend layout
    return render_template("admission.html", enrollment_steps=steps)

@views.route('/scholarship', methods=['GET', 'POST'])
def scholarship_checker():
    feedback_message = None
    
    if request.method == 'POST':
        try:
            # Capture what the student typed into the webpage text box
            user_gwa = float(request.form.get('gwa'))
            # Send it to the backend engine logic rule to get an answer
            feedback_message = scholarship_engine.check_Eligibility(user_gwa)
        except (ValueError, TypeError):
            feedback_message = "Please enter a valid numeric grade format (e.g., 1.75)."

    return render_template("scholarship.html", feedback=feedback_message)