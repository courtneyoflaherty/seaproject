# This file contains hardcoded example data for to initialise upon start up 

from models import db, User, Developer, Project, ProjectAssignments
from werkzeug.security import generate_password_hash
from datetime import date
import json


def example_data():

#   Users Table Data:
    if User.query.count() == 0:
        users = [
            User(first_name="Admin", surname="User", email="admin@example.com", password=generate_password_hash("testtest"), is_admin=True),
            User(first_name="Regular", surname="User", email="user@example.com", password=generate_password_hash("testtest"), is_admin=False),
            User(first_name="Michael", surname="Robinavitch", email="michael.robinavitch@example.com", password=generate_password_hash("testtest"), is_admin=False),
            User(first_name="Heather", surname="Collins", email="heather.collins@example.com", password=generate_password_hash("testtest"), is_admin=False),
            User(first_name="Trinity", surname="Santos", email="trinity.santos@example.com", password=generate_password_hash("testtest"), is_admin=False),
            User(first_name="Frank", surname="Langdon", email="frank.langdon@example.com", password=generate_password_hash("testtest"), is_admin=False),
            User(first_name="Dana", surname="Evans", email="dana.evans@example.com", password=generate_password_hash("test"), is_admin=False),
            User(first_name="Blake", surname="Henderson", email="blake.henderson@example.com", password=generate_password_hash("test   "), is_admin=False),
            User(first_name="Anders", surname="Holmvik", email="anders.holmvik@example.com", password=generate_password_hash("test"), is_admin=False),
            User(first_name="Alan", surname="Sugar", email="alan.sugar@theapprentice.com", password=generate_password_hash("test"), is_admin=True),
        ]
        db.session.add_all(users)
        db.session.commit()

    #   Developers Table Data:
    if Developer.query.count() == 0:
        developers = [
            Developer(first_name="Michael", surname="Robinavitch", email="michael.robinavitch@example.com", skills=json.dumps(["Appian", "Appian RPA"])),
            Developer(first_name="Heather", surname="Collins", email="heather.collins@example.com", skills=json.dumps(["Appian", "Tungsten"])),
            Developer(first_name="Trinity", surname="Santos", email="trinity.santos@example.com", skills=json.dumps(["BluePrism"])),
            Developer(first_name="Frank", surname="Langdon", email="frank.langdon@example.com", skills=json.dumps(["Tungsten"])),
            Developer(first_name="Dana", surname="Evans", email="dana.evans@example.com", skills=json.dumps(["Tungsten"])),
            Developer(first_name="Alan", surname="Sugar", email="alan.sugar@theapprentice.com", skills=json.dumps(["Tungsten"])),
            Developer(first_name="Karen", surname="Brady", email="karen.brady@theapprentice.com", skills=json.dumps(["Tungsten"])),
            Developer(first_name="Blake", surname="Henderson", email="blake.henderson@example.com", skills=json.dumps(["Appian"])),
            Developer(first_name="Anders", surname="Holmvik", email="anders.holmvik@example.com", skills=json.dumps(["Appian"])),
            Developer(first_name="RPA", surname="Legend", email="rpa.legend@example.com", skills=json.dumps(["Appian RPA"])),
            Developer(first_name="Appian", surname="Legend", email="appian.legend@example.com", skills=json.dumps(["Appian"])),
            Developer(first_name="BluePrism", surname="Legend", email="blueprism.legend@example.com", skills=json.dumps(["BluePrism"])),
            Developer(first_name="PowerApps", surname="Legend", email="powerapps.legend@example.com", skills=json.dumps(["Power Apps"])),
            Developer(first_name="Tungsten", surname="Legend", email="tungsten.legend@example.com", skills=json.dumps(["Tungsten"])),
            Developer(first_name="AllTechnologies", surname="Legend", email="alltechnologies.legend@example.com", skills=json.dumps(["Appian", "Appian RPA", "BluePrism", "Power Apps", "Tungsten"])),
            Developer(first_name="MultiTechnology", surname="Legend", email="multitechnology.legend@example.com", skills=json.dumps(["Appian", "Appian RPA", "BluePrism"])),
        ]
        db.session.add_all(developers)
        db.session.commit()

    #   Projects Table Data:
    if Project.query.count() == 0:
        projects = [
            Project(name="The Pitt Revamp", description="Revamp of The Pitt workflows", start_date=date(2025, 10, 27), end_date=date(2080, 1, 1), required_skills=json.dumps(["Appian", "Appian RPA", "BluePrism"])),
            Project(name="Project Apprentice Overhaul", description="Project to overhaul Alan Sugar's means of intelligent document ingestion using Tungsten", start_date=date(2025, 2, 27), end_date=date(2030, 12, 6), required_skills=json.dumps(["Tungsten"])),
            Project(name="Rancho Cucamonga Telemarketing", description="Project to add autonomous Appian agents to streamline the resources required at a telemarketing company", start_date=date(2026, 3, 5), end_date=date(2026, 10, 11), required_skills=json.dumps(["Appian"])),
            Project(name="Appian RPA Project", description="Appian RPA Project for example", start_date=date(2026, 2, 4), end_date=date(2026, 5, 10), required_skills=json.dumps(["Appian", "Appian RPA"])),
            Project(name="BluePrism Project Example", description="BluePrism Project Example Description", start_date=date(2024, 1, 1), end_date=date(2072, 2, 1), required_skills=json.dumps(["BluePrism"])),
            Project(name="Power Apps Example Project", description="Power Apps Example Project Description", start_date=date(2024, 2, 1), end_date=date(2030, 2, 2), required_skills=json.dumps(["Power Apps"])),
            Project(name="Tungsten Project Example", description="Tungsten Project Description", start_date=date(2025, 12, 29), end_date=date(2026, 9, 4), required_skills=json.dumps(["Tungsten"])),
            Project(name="All Technologies Project Example", description="All Technologies Project Example Description", start_date=date(2022, 1, 1), end_date=date(2032, 1, 1), required_skills=json.dumps(["Appian", "Appian RPA", "BluePrism", "Tungsten"])),
            Project(name="Multi-Tech Project Example", description="Multi-Tech Project Example Description", start_date=date(2025, 12, 28), end_date=date(2026, 12, 1), required_skills=json.dumps(["Appian", "Appian RPA", "BluePrism"])),
            Project(name="Project And Another One", description="And Another Project Description", start_date=date(2026, 2, 19), end_date=date(2026, 7, 11), required_skills=json.dumps(["Appian", "Appian RPA"])),
            Project(name="And Another Another One Project", description="And Another Another One Description", start_date=date(2025, 1, 1), end_date=date(2027, 7, 7), required_skills=json.dumps(["Appian", "Tungsten"])),
            Project(name="Power Apps Automation Initiative", description="Initiative to automate internal HR processes using Power Apps", start_date=date(2026, 1, 1), end_date=date(2026, 12, 31), required_skills=json.dumps(["Power Apps"])),
        ]
        db.session.add_all(projects)
        db.session.commit()

    #   Project Assignments Table Data:
    if ProjectAssignments.query.count() == 0:        
        michael = Developer.query.filter_by(email="michael.robinavitch@example.com").first()
        heather = Developer.query.filter_by(email="heather.collins@example.com").first()
        trinity = Developer.query.filter_by(email="trinity.santos@example.com").first()
        frank = Developer.query.filter_by(email="frank.langdon@example.com").first()
        dana = Developer.query.filter_by(email="dana.evans@example.com").first()
        blake = Developer.query.filter_by(email="blake.henderson@example.com").first()
        anders = Developer.query.filter_by(email="anders.holmvik@example.com").first()
        karen = Developer.query.filter_by(email="karen.brady@theapprentice.com").first()
        rpa = Developer.query.filter_by(email="rpa.legend@example.com").first()
        multi = Developer.query.filter_by(email="multitechnology.legend@example.com").first()

        pitt = Project.query.filter_by(name="The Pitt Revamp").first()
        apprentice = Project.query.filter_by(name="Project Apprentice Overhaul").first()
        rancho = Project.query.filter_by(name="Rancho Cucamonga Telemarketing").first()
        appian_rpa = Project.query.filter_by(name="Appian RPA Project").first()
        blueprism = Project.query.filter_by(name="BluePrism Project Example").first()
        tungsten = Project.query.filter_by(name="Tungsten Project Example").first()
        all_tech = Project.query.filter_by(name="All Technologies Project Example").first()
        multi_tech = Project.query.filter_by(name="Multi-Tech Project Example").first()
        another = Project.query.filter_by(name="Project And Another One").first()
        power_apps = Project.query.filter_by(name="Power Apps Automation Initiative").first()

        assignments = [
            ProjectAssignments(developer_id=michael.id, project_id=pitt.id, time_allocation=50.0, assignment_start_date=date(2025, 10, 27), assignment_end_date=date(2026, 6, 1)),
            ProjectAssignments(developer_id=heather.id, project_id=pitt.id, time_allocation=70.0, assignment_start_date=date(2025, 10, 27), assignment_end_date=date(2026, 6, 1)),
            ProjectAssignments(developer_id=trinity.id, project_id=pitt.id, time_allocation=60.0, assignment_start_date=date(2025, 10, 27), assignment_end_date=date(2026, 6, 1)),
            ProjectAssignments(developer_id=frank.id, project_id=apprentice.id, time_allocation=80.0, assignment_start_date=date(2025, 2, 27), assignment_end_date=date(2026, 12, 6)),
            ProjectAssignments(developer_id=dana.id, project_id=apprentice.id, time_allocation=50.0, assignment_start_date=date(2025, 2, 27), assignment_end_date=date(2026, 12, 6)),
            ProjectAssignments(developer_id=blake.id, project_id=rancho.id, time_allocation=100.0, assignment_start_date=date(2026, 3, 5), assignment_end_date=date(2026, 10, 11)),
            ProjectAssignments(developer_id=anders.id, project_id=appian_rpa.id, time_allocation=75.0, assignment_start_date=date(2026, 2, 4), assignment_end_date=date(2026, 5, 10)),
            ProjectAssignments(developer_id=rpa.id, project_id=appian_rpa.id, time_allocation=100.0, assignment_start_date=date(2026, 2, 4), assignment_end_date=date(2026, 5, 10)),
            ProjectAssignments(developer_id=trinity.id, project_id=blueprism.id, time_allocation=50.0, assignment_start_date=date(2024, 1, 1), assignment_end_date=date(2025, 1, 1)),
            ProjectAssignments(developer_id=karen.id, project_id=tungsten.id, time_allocation=60.0, assignment_start_date=date(2025, 12, 29), assignment_end_date=date(2026, 9, 4)),
            ProjectAssignments(developer_id=multi.id, project_id=all_tech.id, time_allocation=90.0, assignment_start_date=date(2022, 1, 1), assignment_end_date=date(2032, 1, 1)),
            ProjectAssignments(developer_id=michael.id, project_id=another.id, time_allocation=40.0, assignment_start_date=date(2026, 2, 19), assignment_end_date=date(2026, 7, 11)),
            ProjectAssignments(developer_id=heather.id, project_id=multi_tech.id, time_allocation=55.0, assignment_start_date=date(2025, 12, 28), assignment_end_date=date(2026, 12, 1)),
        ]
        db.session.add_all(assignments)
        db.session.commit()