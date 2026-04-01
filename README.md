<<<<<<< HEAD
# Project Title
Aviva Project Allocation Tracker - a proof of concept of a project allocation tracking system

## Description
This was designed as part of the Software Engineering & Agile course, aiming to resolve the business problem of relying on a singular spreadsheet with limited access, by replacing it with a live web application

### Dependencies
This application has a pre-built virtual environment included, however, any issues with running this would require the following installations:

Python version:
3.13.12

Outlined in requirements.txt and include:
blinker==1.9.0
click==8.3.1
colorama==0.4.6
Flask==3.1.3
Flask-SQLAlchemy==3.1.1
greenlet==3.3.2
gunicorn==25.3.0
iniconfig==2.3.0
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
packaging==26.0
pluggy==1.6.0
Pygments==2.20.0
pytest==9.0.2
SQLAlchemy==2.0.48
typing_extensions==4.15.0
Werkzeug==3.1.7

This was developed on Windows so users are advised to run on the same OS if running locally.
Alternatively this will also be hosted online via Render.

### Executing application
1) Download the project and open in your IDE of choice
2) Open a terminal in the project root level
3) Activate the virtual environment by inputting in terminal:
   venv\Scripts\activate
4) Run the application locally by inputting in terminal:
   python app.py
5) Upon a successful terminal message, open a web browser and navigate to:
   http://127.0.0.1:5000/
6) The application should be running successfully now. Any issues please run the following in terminal:
   python -m venv venv 
   venv\Scripts\activate 
   pip install -r requirements.txt
7) The database will initialise with example data each time so the .db file can be deleted and will rebuild everytime the 'python app.py' command is entered to support testing and demonstration

then run:
   python app.py

### Navigating the application
1) Users will be taken to an index homepage. From here either navigate to 'login' or 'sign up''
2) Upon a successful login, users are taken to a 'project overview' page. From here, regular users can read all entries on the page, or navigate to a 'developers overview' page by pressing a button to show a similar view, or 'logout' of the application.
3) Admin users are able to navigate from both the project overview page and the developer overview page to edit or delete the entries displayed. Edits will allow users to adjust the data within a form and then complete, while deletions will display a read-only copy of the data and then require additional confirmation.
4) Admin users can also create new project and developer entries via the associated buttons on the overview pages.
5) Assigned developer details do not need to be input on the 'add project' or 'edit project' pages, unless some of the developer information is input, then all must be completed.
6) From any of the create/edit/delete pages, admin users can their choices via a 'submit' button or return to the previous page via a 'cancel' button.
7) Additionally, admin users will see in the top right of the screen of all pages a 'user management' button. This allows for navigation to the 'user management' screen. From here admin users only will be able to see all registered user accounts and then navigate to 'edit' or 'delete' screens for the user entries in addition.
8) If users attempt to navigate to a non-existant page then a 404 will be triggered.
9) A 500 page additionally exists for robust error handling.

### Example credentials
1) For demonstration purposes the following credentials can be used at the log in page:
2) Admin (full CRUD functionality):
      email: admin@example.com
      password: testtest

2) Regular User (read-only):
   email: user@example.com
   password: testtest  

### Executing tests
1) Activate the virtual environment with the same steps as above
2) Open terminal 
3) Type in the terminal:
   pytest
This will give basic testing coverage
4) Type in the terminal:
   pytest -v
This will give more verbose outputs of testing results

## Authors
Courtney O'Flaherty
=======
# seaproject
Software Engineering and Agile project
>>>>>>> c602268b3b5e511232d0b1383c28ff1879758d73
