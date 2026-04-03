# This file is used to define the database models and schema for the application

# Import libraries and modules:
from flask_sqlalchemy import SQLAlchemy
from datetime import date

# Flask setup:
# Links to SQLAchemy and database file
db = SQLAlchemy()

# Database schema:

class User(db.Model):
    id = db.Column(db.INT, primary_key=True, autoincrement=True, nullable=False)
    first_name = db.Column(db.VARCHAR(100), nullable=False)
    surname = db.Column(db.VARCHAR(100), nullable=False)
    email = db.Column(db.VARCHAR(100), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(200), nullable=False)
    is_admin= db.Column(db.BOOLEAN, nullable=False, default=False)

class Developer(db.Model):
    id = db.Column(db.INT, primary_key=True, autoincrement=True, nullable=False)
    first_name = db.Column(db.VARCHAR(100), nullable=False)
    surname = db.Column(db.VARCHAR(100), nullable=False)
    email = db.Column(db.VARCHAR(100), unique=True, nullable=False)
    skills = db.Column(db.JSON, nullable=False)
    # This was added so that developers can be added as an entry without needing a user account (hence being nullable) with the intention that developers can later sign up for a user account and be linked to their developer entry. This was not fully implemented, but was left to support future development. 
    user_id = db.Column(db.INT, db.ForeignKey('user.id'), nullable=True)

class Project(db.Model):
    id = db.Column(db.INT, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.VARCHAR(100), nullable=False)
    description = db.Column(db.VARCHAR(255), nullable=False)
    start_date = db.Column(db.DATE, nullable=False)
    end_date = db.Column(db.DATE, nullable=False)
    required_skills = db.Column(db.JSON)

class ProjectAssignments(db.Model):
    id = db.Column(db.INT, primary_key=True, autoincrement=True, nullable=False)
    developer_id = db.Column(db.INT, db.ForeignKey('developer.id'), nullable=True)
    project_id = db.Column(db.INT, db.ForeignKey('project.id'), nullable=False)
    time_allocation = db.Column(db.FLOAT, nullable=True)
    assignment_start_date = db.Column(db.DATE, nullable=True)
    assignment_end_date = db.Column(db.DATE, nullable=True)