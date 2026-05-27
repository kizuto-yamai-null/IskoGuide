# website/views.py
from flask import Blueprint, render_template, request, redirect, url_for

# 1. Import all 5 structural skeleton modules you created
from modules.admission import AdmissionModule
from modules.scholarship import ScholarshipModule
from modules.directory import CampusDirectory
from modules.forum import ForumModule
from modules.about import AboutModule

views = Blueprint('views', __name__)

# 2. Instantiate all engines so they are globally ready to process data
admission_engine = AdmissionModule()
scholarship_engine = ScholarshipModule()
directory_engine = CampusDirectory()
forum_engine = ForumModule()
about_engine = AboutModule()


# ==================================================
#               CORE PUBLIC ROUTES
# ==================================================

@views.route('/')
def home():
    return render_template("home.html")


@views.route('/admission')
def admission_guide():
    # Fetches the structural steps from your module layer
    steps = admission_engine.show_Enrollment_Guide()
    requirements = admission_engine.list_Requirements(gwa=1.0) # Placeholder call
    return render_template("admission.html", enrollment_steps=steps, requirements=requirements)


@views.route('/scholarship', methods=['GET', 'POST'])
def scholarship_checker():
    feedback_message = None
    grants = scholarship_engine.list_Available_Grants()
    timelines = scholarship_engine.show_Timelines()
    
    if request.method == 'POST':
        try:
            # Capture the student's entered GWA from the form text box
            user_gwa = float(request.form.get('gwa'))
            # Evaluate eligibility using your backend rules
            feedback_message = scholarship_engine.check_Eligibility(user_gwa)
        except (ValueError, TypeError):
            feedback_message = "Please enter a valid numeric grade format (e.g., 1.75)."

    return render_template(
        "scholarship.html", 
        feedback=feedback_message, 
        grants=grants, 
        timelines=timelines
    )


# ==================================================
#           NEWLY CONNECTED SUBMODULES
# ==================================================

@views.route('/directory')
def campus_directory():
    # Grab the layout lists from Enrico's directory skeleton
    landmarks_list = directory_engine.show_Landmarks()
    shops_list = directory_engine.get_Shop_Locations()
    
    # Pass them directly to Dustin and Laud's UI frontend templates
    return render_template(
        "directory.html", 
        landmarks=landmarks_list, 
        shops=shops_list
    )


@views.route('/forum', methods=['GET', 'POST'])
def student_forum():
    # Handle a new post submission if an authorized user submits a form
    if request.method == 'POST':
        post_content = request.form.get('content')
        if post_content:
            # Mock username for now until your login flow handles actual user session states
            forum_engine.create_Post(username="AnonymousIsko", content=post_content)
            return redirect(url_for('views.student_forum'))

    # Fetch all active discussion threads to list them out on the UI
    active_posts = forum_engine.view_threads()
    return render_template("forum.html", posts=active_posts)


@views.route('/about')
def about_credits():
    # Fetch school description and emergency/office email contacts
    description = about_engine.show_School_Credits()
    contacts = about_engine.show_Campus_Contacts()
    
    return render_template(
        "about.html", 
        school_description=description, 
        campus_contacts=contacts
    )