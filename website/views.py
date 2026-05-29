# website/views.py
from flask import Blueprint, render_template, request, redirect, url_for

# Import the module engines
from modules.admission import AdmissionModule
from modules.scholarship import ScholarshipModule
from modules.directory import CampusDirectory
from modules.forum import ForumModule
from modules.about import AboutModule

views = Blueprint('views', __name__)

# Initialize global engines to process data behind the scenes
admission_engine = AdmissionModule()
scholarship_engine = ScholarshipModule()
directory_engine = CampusDirectory()
forum_engine = ForumModule()
about_engine = AboutModule()


# ==================================================
#               MAIN PAGES AND ROUTES
# ==================================================

@views.route('/')
def home():
    return render_template("index.html")


@views.route('/admission', methods=["GET", "POST"])
def admission_guide():
    # Get standard steps and requirements
    steps = admission_engine.show_Enrollment_Guide()
    requirements = admission_engine.list_Requirements(gwa=1.0)
    
    evaluation_result = None
    
    # Process the document checklist when the user submits the form
    if request.method == 'POST':
        student_type = request.form.get('student_type')
        submitted_docs = request.form.getlist('documents') 
        
        # Check which documents are missing
        evaluation_result = admission_engine.check_submission_eligibility(student_type, submitted_docs)
    
    return render_template(
        "admission.html", 
        enrollment_steps=steps, 
        requirements=requirements,
        evaluation=evaluation_result
    )


@views.route('/scholarship', methods=['GET', 'POST'])
def scholarship_checker():
    # Get guidelines and deadlines
    guidelines = scholarship_engine.get_grant_guidelines()
    timelines = scholarship_engine.get_deadlines()
    
    evaluation_result = None
    
    # Process the qualification form when the user submits their grades and income
    if request.method == 'POST':
        try:
            user_gwa = float(request.form.get('gwa'))
            user_income = float(request.form.get('income'))
            scholarship_type = request.form.get('scholarship_type')
            
            # Evaluate if the user qualifies based on grades and family income
            evaluation_result = scholarship_engine.evaluate_eligibility(user_gwa, user_income, scholarship_type)
        except (ValueError, TypeError):
            evaluation_result = {
                "is_eligible": False,
                "status_message": "Please enter valid numbers for GWA and Income formats."
            }

    return render_template(
        "scholarship.html", 
        evaluation=evaluation_result, 
        guidelines=guidelines, 
        timelines=timelines
    )


# ==================================================
#         CAMPUS LIFE AND STUDENT SUBMODULES
# ==================================================

@views.route('/forStudent', methods=['GET', 'POST'])
def campus_directory():
    # Load base landmarks and shops for initial viewing
    landmarks_list = directory_engine.show_Landmarks()
    shops_list = directory_engine.get_Shop_Locations()
    
    search_results = None
    query_string = ""
    
    # Filter the list if the user types something into the search bar
    if request.method == 'POST':
        query_string = request.form.get('search_query', '').strip()
        search_results = directory_engine.search_campus_directory(query_string)
        
    return render_template(
        "forStudent.html", 
        landmarks=landmarks_list, 
        shops=shops_list,
        search_results=search_results,
        query=query_string
    )


@views.route('/forum', methods=['GET', 'POST'])
def student_forum():
    # Create a new discussion post
    if request.method == 'POST':
        post_content = request.form.get('content')
        if post_content:
            forum_engine.create_Post(username="AnonymousIsko", content=post_content)
            return redirect(url_for('views.student_forum'))

    # Load and display active discussion threads
    active_posts = forum_engine.view_threads()
    return render_template("forum.html", posts=active_posts)


@views.route('/aboutPUP')
def about_credits():
    # Load and display static university info and contact links
    description = about_engine.show_School_Credits()
    contacts = about_engine.show_Campus_Contacts()
    
    return render_template(
        "aboutPUP.html", 
        school_description=description, 
        campus_contacts=contacts
    )