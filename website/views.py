# website/views.py
from flask import Blueprint, render_template, request, redirect, url_for, session

# Share the single initialized master controller state from your auth configuration
from website.auth import controller

views = Blueprint('views', __name__)

# ==================================================
#                  MAIN PAGES AND ROUTES
# ==================================================

@views.route('/')
@views.route('/home') # 🏢 FIX: Added alias so Dustin's navbar link doesn't break
def home():
    role_num = session.get('role', 4)
    role_labels = {1: "Admin", 2: "Moderator", 3: "Student", 4: "Visitor"}
    return render_template("index.html", role=role_labels.get(role_num, "Visitor"))


@views.route('/admission', methods=["GET", "POST"])
def admission_guide():
    # Use the centralized controller instance to keep memory uniform across the app
    steps = controller.admission_module.show_Enrollment_Guide()
    requirements = controller.admission_module.list_Requirements(gwa=1.0)
    
    evaluation_result = None
    
    if request.method == 'POST':
        student_type = request.form.get('student_type')
        submitted_docs = request.form.getlist('documents') 
        
        evaluation_result = controller.admission_module.check_submission_eligibility(student_type, submitted_docs)
    
    return render_template(
        "admission.html", 
        enrollment_steps=steps, 
        requirements=requirements,
        evaluation=evaluation_result
    )


@views.route('/scholarship', methods=['GET', 'POST'])
def scholarship_checker():
    guidelines = controller.scholarship_module.get_grant_guidelines()
    timelines = controller.scholarship_module.get_deadlines()
    
    evaluation_result = None
    
    if request.method == 'POST':
        try:
            user_gwa = float(request.form.get('gwa'))
            user_income = float(request.form.get('income'))
            scholarship_type = request.form.get('scholarship_type')
            
            evaluation_result = controller.scholarship_module.evaluate_eligibility(user_gwa, user_income, scholarship_type)
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
    landmarks_list = controller.campus_directory.show_Landmarks()
    shops_list = controller.campus_directory.get_Shop_Locations()
    
    search_results = None
    query_string = ""
    
    if request.method == 'POST':
        query_string = request.form.get('search_query', '').strip()
        search_results = controller.campus_directory.search_campus_directory(query_string)
        
    return render_template(
        "forStudent.html", 
        landmarks=landmarks_list, 
        shops=shops_list,
        search_results=search_results,
        query=query_string
    )


@views.route('/forum', methods=['GET', 'POST'])
def student_forum():
    """
    Handles rendering the forum ecosystem. Enforces Task 3 verification restrictions
    and catches spam inputs through your custom bilingual filter engine.
    """
    # 1. Grab current login status tokens (Defaults to Role 4: Visitor)
    current_role = session.get('role', 4)
    user_email = session.get('user_email', "Guest_User")
    
    error_message = None

    # 2. Process form submission attempts
    if request.method == 'POST':
        # 🔐 SAFETY GATE: Block Guests from pushing backend writes entirely
        if current_role == 4:
            active_posts = controller.forum_module.view_threads()
            return render_template("forum.html", posts=active_posts, role=current_role, error="Access Denied: Visitors are limited to VIEW-ONLY access.")
        
        # Pull text components from Dustin's front-end input forms
        post_title = request.form.get('title', 'Campus Discussion')
        post_content = request.form.get('content')
        
        if post_content:
            # Send the input directly into your forum filter and pending queue pipeline
            success, message = controller.forum_module.create_Post(user_email, post_title, post_content)
            
            if not success:
                error_message = message  # Capture the "Profanity Detected" warning block
            else:
                return redirect(url_for('views.student_forum'))

    # 3. Handle GET deliveries
    active_posts = controller.forum_module.view_threads()
    return render_template(
        "forum.html", 
        posts=active_posts, 
        role=current_role, 
        user_email=user_email, 
        error=error_message
    )


@views.route('/aboutPUP')
def about_credits():
    description = controller.about_module.show_School_Credits()
    contacts = controller.about_module.show_Campus_Contacts()
    
    return render_template(
        "aboutPUP.html", # 📝 NOTE: Matches your sidebar's template file exactly
        school_description=description, 
        campus_contacts=contacts
    )