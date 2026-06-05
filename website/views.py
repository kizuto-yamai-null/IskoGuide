# website/views.py
from flask import Blueprint, render_template, request, redirect, url_for, session

from website.auth import controller

views = Blueprint('views', __name__)


@views.route('/')
@views.route('/home')
def home():
    role_num = session.get('role', 4)
    role_labels = {1: "Admin", 2: "Moderator", 3: "Student", 4: "Visitor"}
    return render_template("index.html", role=role_labels.get(role_num, "Visitor"))


@views.route('/admission', methods=['GET', 'POST'])
def admission_guide():
    requirements_pool = controller.admission_module.requirements_pool
    selected_track = request.form.get('student_type', 'Freshman')
    submitted_docs = request.form.getlist('submitted_docs')
    checklist_result = None

    if request.method == 'POST':
        checklist_result = controller.admission_module.check_submission_eligibility(
            selected_track,
            submitted_docs
        )

    return render_template(
        "admission.html",
        requirements_pool=requirements_pool,
        selected_track=selected_track,
        submitted_docs=submitted_docs,
        checklist_result=checklist_result
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
            evaluation_result = controller.scholarship_module.evaluate_eligibility(
                user_gwa,
                user_income,
                scholarship_type
            )
        except (ValueError, TypeError):
            evaluation_result = {
                "is_eligible": False,
                "status_message": "Please enter valid numbers for GWA and income."
            }

    return render_template(
        "scholarship.html",
        evaluation=evaluation_result,
        guidelines=guidelines,
        timelines=timelines,
        scholarship_options=list(timelines.keys()),
        selected_scholarship=request.form.get(
            'scholarship_type', '') if request.method == 'POST' else '',
        submitted_gwa=request.form.get(
            'gwa', '') if request.method == 'POST' else '',
        submitted_income=request.form.get(
            'income', '') if request.method == 'POST' else ''
    )


@views.route('/forStudent', methods=['GET', 'POST'])
def campus_directory():
    landmarks_list = controller.campus_directory.show_Landmarks()
    shops_list = controller.campus_directory.get_Shop_Locations()
    search_results = None
    query_string = ""

    if request.method == 'POST':
        query_string = request.form.get('search_query', '').strip()
        search_results = controller.campus_directory.search_campus_directory(
            query_string)

    return render_template(
        "forStudent.html",
        landmarks=landmarks_list,
        shops=shops_list,
        search_results=search_results,
        query=query_string
    )


@views.route('/forum', methods=['GET', 'POST'])
def student_forum():
    current_role = session.get('role', 4)
    user_email = session.get('user_email', "Guest_User")
    error_message = None
    notice_message = session.pop('forum_notice', None)
    forum_query = request.args.get('q', '').strip()

    if request.method == 'POST':
        action = request.form.get('action', 'create')

        if action in ('approve', 'reject'):
            if current_role not in (1, 2):
                error_message = "Only Admins and Moderators can manage pending posts."
            else:
                try:
                    post_id = int(request.form.get('post_id', 0))
                    if action == 'approve':
                        was_updated = controller.forum_module.approve_post(
                            post_id)
                        session['forum_notice'] = "Post approved." if was_updated else "Post was not found."
                    else:
                        was_updated = controller.forum_module.reject_post(
                            post_id)
                        session['forum_notice'] = "Post rejected." if was_updated else "Post was not found."
                    return redirect(url_for('views.student_forum'))
                except (ValueError, TypeError):
                    error_message = "Invalid post selected."

        elif action == 'report':
            if current_role == 4:
                error_message = "Visitors cannot report posts."
            else:
                try:
                    post_id = int(request.form.get('post_id', 0))
                    was_reported = controller.forum_module.report_Post(post_id)
                    session['forum_notice'] = "Post reported for review." if was_reported else "Post was not found."
                    return redirect(url_for('views.student_forum'))
                except (ValueError, TypeError):
                    error_message = "Invalid post selected."

        elif action == 'reply':
            if current_role not in (1, 2):
                error_message = "Only Admins and Moderators can reply to posts."
            else:
                try:
                    post_id = int(request.form.get('post_id', 0))
                    reply_content = request.form.get(
                        'reply_content', '').strip()
                    success, message = controller.forum_module.add_reply(
                        post_id,
                        user_email,
                        reply_content
                    )
                    if success:
                        session['forum_notice'] = message
                        return redirect(url_for('views.student_forum') + f"#post-{post_id}")
                    error_message = message
                except (ValueError, TypeError):
                    error_message = "Invalid post selected."

        elif action == 'create':
            if current_role == 4:
                error_message = "Visitors are limited to view-only access. Log in to submit a post."
            else:
                post_title = request.form.get('title', 'Campus Discussion')
                post_content = request.form.get('content', '').strip()

                if not post_content:
                    error_message = "Please write a post before submitting."
                else:
                    success, message = controller.forum_module.create_Post(
                        user_email,
                        post_title,
                        post_content
                    )
                    if success:
                        session['forum_notice'] = message
                        return redirect(url_for('views.student_forum'))
                    error_message = message
        else:
            error_message = "Unknown forum action."

    active_posts = controller.forum_module.view_threads()
    displayed_posts = active_posts

    if forum_query:
        clean_query = forum_query.lower()
        displayed_posts = [
            post for post in active_posts
            if clean_query in post.get('title', '').lower()
            or clean_query in post.get('content', '').lower()
            or clean_query in post.get('author', '').lower()
            or any(
                clean_query in reply.get('content', '').lower()
                or clean_query in reply.get('author', '').lower()
                for reply in post.get('replies', [])
            )
        ]

    total_replies = sum(len(post.get('replies', [])) for post in active_posts)
    pending_posts = controller.forum_module.get_pending_queue(
    ) if current_role in (1, 2) else []
    return render_template(
        "forum.html",
        posts=displayed_posts,
        total_posts=len(active_posts),
        total_replies=total_replies,
        role=current_role,
        user_email=user_email,
        pending_posts=pending_posts,
        forum_query=forum_query,
        notice=notice_message,
        error=error_message
    )


@views.route('/aboutPUP')
def about_credits():
    description = controller.about_module.show_School_Credits()
    contacts_package = controller.about_module.show_Campus_Contacts()

    return render_template(
        "aboutPUP.html",
        school_description=description,
        social_channels=contacts_package["socials"],
        helpdesk_offices=contacts_package["offices"]
    )
