# This file is used for the main Flask app setup, including routing, data validation, and overall application logic

# Import libraries and modules:
from flask import Flask, json, render_template, request, redirect, url_for, flash, session, abort
from flask_sqlalchemy import SQLAlchemy  
import secrets                           
import re                     
from functools import wraps              
from werkzeug.security import generate_password_hash, check_password_hash  
from datetime import date     

# Imports models once the database has been initialised to prevent calling multiple SQLAlchemy instances
from models import db, User, Developer, Project, ProjectAssignments
 
# Creates the app, configure the database, and enable setting a secret key for secure sessions
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Connect SQLAlchemy to the app
db.init_app(app)
with app.app_context():
    db.create_all()
from example_data import example_data    
with app.app_context():
    example_data()

# Login Required:
def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if session.get('user_id') is None:
            flash('Please log in to proceed.')
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return wrapped

# Admin Required:
def admin_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if session.get('user_id') is None:
            flash('Please log in to access that page.')
            return redirect(url_for('login'))
        if not session.get('is_admin'):
            flash('Admin access is required for that action.')
            return redirect(url_for('project_view'))
        return view(*args, **kwargs)
    return wrapped

# Data Input Validation Functions:
# Email address
def validate_email_address(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        raise ValueError("ERROR: Invalid email address format.")
    return email

# Name
def sanitise_name(name):
    pattern = r"^[a-zA-Z\s\-']+$"
    if not re.match(pattern, name):
        raise ValueError("ERROR: Names can only contain letters, spaces, hyphens, and apostrophes.")
    return name

# Flask Routing:
# Generic pages first:
# Index/home page:
@app.route('/')
def index():
    return render_template('index.html')

# Sign up:
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            flash("ERROR: Passwords do not match.")
            return redirect(url_for('signup'))
        if User.query.filter_by(email=email).first():
            flash("ERROR: Email already in use.")
            return redirect(url_for('signup'))
        hashed_password = generate_password_hash(password)
        new_user = User(first_name=first_name, surname=surname, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("SUCCESS: Account creation successful! Please navigate to log in page.")
        return redirect(url_for('login'))
    return render_template('signup.html')

# Login:
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['user_name'] = f"{user.first_name} {user.surname}"
            session['is_admin'] = bool(user.is_admin)
            flash(f"Welcome {user.first_name} {user.surname}!")
            return redirect(url_for('project_view'))
        else:
            flash("ERROR: Invalid email or password combination.")
            return redirect(url_for('login'))
    return render_template('login.html')

# Logout:
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('is_admin', None)
    flash('SUCCESS: You have been logged out.')
    return render_template('logout.html')

# Overview Pages:
# Project Overview
@app.route('/projectview', methods=['GET'])
@login_required
def project_view():
    projects = Project.query.all()
    developers = Developer.query.all()
    project_assignments = ProjectAssignments.query.all()
    return render_template('project_view.html', projects=projects, developers=developers, assignments=project_assignments)

# Developer Overview
@app.route('/developerview', methods=['GET'])
@login_required
def developer_view():
    projects = Project.query.all()
    developers = Developer.query.all()
    project_assignments = ProjectAssignments.query.all()
    return render_template('developer_view.html', projects=projects, developers=developers, assignments=project_assignments)

# User Management (Admin-Only view)
@app.route('/user_management', methods=['GET', 'POST'])
@admin_required
def user_management():
    users = User.query.all()
    return render_template('user_management.html', users=users)

# CRUD Functionality:
# Create:
# Add Project
@app.route('/addproject', methods=['GET', 'POST'])
@admin_required
def add_project():
    if request.method == 'POST':
        try:
            project_name = sanitise_name(request.form['name'])
        except ValueError as e:
            flash(str(e))
            return redirect(url_for('add_project'))
        selected_skills = request.form.getlist('required_skills')
        new_project = Project(
            name=request.form.get('name'),
            description=request.form.get('description'),
            start_date=date.fromisoformat(request.form.get('start_date')),
            end_date=date.fromisoformat(request.form.get('end_date')),
            required_skills=json.dumps(selected_skills)        )
        db.session.add(new_project)
        db.session.commit()

        # Optionally assign a developer to the project at creation time or leave blank for later assignment
        assigned_developer = request.form.get('assigned_developer', '')
        if assigned_developer:
            allocation = request.form.get('time_allocation', '0')
            assign_start = request.form.get('assignment_start', None)
            assign_end = request.form.get('assignment_end', None)
            new_assignments = ProjectAssignments(
                developer_id=assigned_developer,
                project_id=new_project.id,
                time_allocation=float(allocation) if allocation else 0.0,
                assignment_start_date=date.fromisoformat(assign_start) if assign_start else None,
                assignment_end_date=date.fromisoformat(assign_end) if assign_end else None
            )
            db.session.add(new_assignments)
            db.session.commit()

        flash("SUCCESS: Project added!")
        return redirect(url_for('project_view'))
    projects = Project.query.all()
    developers = Developer.query.all()
    assignments = ProjectAssignments.query.all()
    return render_template(
        'add_project.html',
        projects=projects,
        developers=developers,
        assignments=assignments
    )

#Add Developer
@app.route('/adddeveloper', methods=['GET', 'POST'])
@admin_required
def add_developer():
    if request.method == 'POST':
        try:
            first_name = sanitise_name(request.form['first_name'])
            surname = sanitise_name(request.form['surname'])
            email = validate_email_address(request.form['email'])
        except ValueError as e:
            flash(str(e))
            return redirect(url_for('add_developer'))
        selected_skills = request.form.getlist('skills')

        new_developer = Developer(
            first_name=first_name,
            surname=surname,
            email=email,
            skills=json.dumps(selected_skills) 
        )
        db.session.add(new_developer)
        db.session.commit()
        flash("SUCCESS: Developer added!")
        return redirect(url_for('developer_view'))
    return render_template('add_developer.html')

# Update:
# Edit Project
@app.route('/edit_project/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit_project(id):
    project = db.session.get(Project, id) or abort(404)
    developers = Developer.query.all()
    assignment = ProjectAssignments.query.filter_by(project_id=project.id).first()
    try:
        skills_list = json.loads(project.required_skills) if project.required_skills else []
    except ValueError:
        skills_list = []
    if request.method == 'POST':
        project.name = request.form['name']
        project.description = request.form['description']
        project.start_date = date.fromisoformat(request.form['start_date'])
        project.end_date = date.fromisoformat(request.form['end_date'])
        project.required_skills = json.dumps(request.form.getlist('required_skills'))
        assigned_developer = request.form.get('assigned_developer', '')
        if assigned_developer:
            allocation = request.form.get('time_allocation', '0')
            assign_start = request.form.get('assignment_start', None)
            assign_end = request.form.get('assignment_end', None)
            if assignment:
                assignment.developer_id = assigned_developer
                assignment.time_allocation = float(allocation) if allocation else 0.0
                assignment.assignment_start_date = date.fromisoformat(assign_start) if assign_start else None
                assignment.assignment_end_date = date.fromisoformat(assign_end) if assign_end else None
            else:
                new_assignment = ProjectAssignments(
                    developer_id=assigned_developer,
                    project_id=project.id,
                    time_allocation=float(allocation) if allocation else 0.0,
                    assignment_start_date=date.fromisoformat(assign_start) if assign_start else None,
                    assignment_end_date=date.fromisoformat(assign_end) if assign_end else None
                )
                db.session.add(new_assignment)
        else:
            if assignment:
                db.session.delete(assignment)
        db.session.commit()
        flash('SUCCESS: Project updated successfully.')
        return redirect(url_for('project_view'))
    return render_template(
        'edit_project.html',
        project=project,
        developers=developers,
        assignment=assignment,
        skills_list=skills_list
    )

# Edit Developer
@app.route('/edit_developer/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit_developer(id):
    developer = db.session.get(Developer, id) or abort(404)
    if request.method == 'POST':
        developer.first_name = request.form['first_name']
        developer.surname = request.form['surname']
        developer.email = request.form['email']
        developer.skills = json.dumps(request.form.getlist('skills'))
        db.session.commit()
        flash('Developer updated successfully.')
        return redirect(url_for('developer_view'))
    return render_template('edit_developer.html', developer=developer)

# Edit User
@app.route('/edit_user/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit_user(id):
    user = db.session.get(User, id) or abort(404)
    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.surname = request.form['surname']
        user.email = request.form['email']
        db.session.commit()
        flash('SUCCESS: User updated successfully.')
        return redirect(url_for('user_management'))
    return render_template('edit_user.html', user=user)


# Delete Functionality:
# Delete Project
@app.route('/delete_project/<int:id>', methods=['GET', 'POST'])
@admin_required
def delete_project(id):
    project = db.session.get(Project, id)
    if not project:
        flash('ERROR: Project not found.')
        return redirect(url_for('project_view'))
    if request.method == 'POST':
        assignments = ProjectAssignments.query.filter_by(project_id=project.id).all()
        for assign in assignments:
            db.session.delete(assign)
        db.session.delete(project)
        db.session.commit()
        flash('SUCCESS: Project deleted.')
        return redirect(url_for('project_view'))
    return render_template('delete_project.html', project=project, assignment=ProjectAssignments.query.filter_by(project_id=project.id).first())

# Delete Developer:
@app.route('/delete_developer/<int:id>', methods=['GET', 'POST'])
@admin_required
def delete_developer(id):
    developer = db.session.get(Developer, id)
    if not developer:
        flash('ERROR: Developer not found.')
        return redirect(url_for('developer_view'))
    if request.method == 'POST':
        assignments = ProjectAssignments.query.filter_by(developer_id=developer.id).all()
        for assign in assignments:
            db.session.delete(assign)
        db.session.delete(developer)
        db.session.commit()
        flash('SUCCESS: Developer deleted.')
        return redirect(url_for('developer_view'))
    return render_template('delete_developer.html', developer=developer, assignment=ProjectAssignments.query.filter_by(developer_id=developer.id).first())

# Delete User:
@app.route('/delete_user/<int:id>', methods=['GET', 'POST'])
@admin_required
def delete_user(id):
    user = db.session.get(User, id)
    if not user:
        flash('ERROR: User not found.')
        return redirect(url_for('user_management'))
    # Additional validation to prevent the default admin account from being deleted
    if user.email == 'admin@example.com':
        flash('ERROR: The default admin account cannot be deleted.')
        return redirect(url_for('user_management'))
    if request.method == 'POST':
        db.session.delete(user)
        db.session.commit()
        flash(f'SUCCESS: User {user.first_name} {user.surname} deleted.')
        return redirect(url_for('user_management'))
    return render_template('delete_user.html', user=user)

# Custom error pages:
# 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Run the app/set debug mode
if __name__ == "__main__":
    app.run(debug=True)