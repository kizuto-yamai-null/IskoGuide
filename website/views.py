# website/views.py
from flask import Blueprint, render_template, request, redirect, url_for

# 1. Import all 5 of your structural module engines
from modules.admission import AdmissionModule
from modules.scholarship import ScholarshipModule
from modules.directory import CampusDirectory
from modules.forum import ForumModule
from modules.about import AboutModule

views = Blueprint('views', __name__)

# 2. Instantiate your global engines to process data behind the scenes
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
    # Adapted to Dustin's master parent layout framework
    return render_template("index.html")


@views.route('/admission')
def admission_guide():
    # Feeds structural steps from your module layer into his admission template
    steps = admission_engine.show_Enrollment_Guide()
    requirements = admission_engine.list_Requirements(gwa=1.0)
    return render_template("admission.html", enrollment_steps=steps, requirements=requirements)


@views.route('/scholarship', methods=['GET', 'POST'])
def scholarship_checker():
    feedback_message = None
    grants = scholarship_engine.list_Available_Grants()
    timelines = scholarship_engine.show_Timelines()
    
    if request.method == 'POST':
        try:
            user_gwa = float(request.form.get('gwa'))
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
#       ADAPTED SUBMODULES (MATCHING UI PATHS)
# ==================================================

@views.route('/forStudent')
def campus_directory():
    # Maps your directory logic straight into his dashboard layout
    landmarks_list = directory_engine.show_Landmarks()
    shops_list = directory_engine.get_Shop_Locations()
    
    return render_template(
        "forStudent.html", 
        landmarks=landmarks_list, 
        shops=shops_list
    )


@views.route('/forum', methods=['GET', 'POST'])
def student_forum():
    if request.method == 'POST':
        post_content = request.form.get('content')
        if post_content:
            forum_engine.create_Post(username="AnonymousIsko", content=post_content)
            return redirect(url_for('views.student_forum'))

    active_posts = forum_engine.view_threads()
    return render_template("forum.html", posts=active_posts)


@views.route('/aboutPUP')
def about_credits():
    # Safeguards your department contacts inside his custom about layout
    description = about_engine.show_School_Credits()
    contacts = about_engine.show_Campus_Contacts()
    
    return render_template(
        "aboutPUP.html", 
        school_description=description, 
        campus_contacts=contacts
    )