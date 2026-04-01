# This test checks that the Flask routing is working correctly for all specified URLs by status code:
import pytest
from app import app

# These should return a 200 as they should work for all users regardless of login status:
def test_index_page():
    assert app.test_client().get('/').status_code == 200

def test_login_page():
    assert app.test_client().get('/login').status_code == 200

def test_signup_page():
    assert app.test_client().get('/signup').status_code == 200

def test_logout_page():
    assert app.test_client().get('/logout').status_code == 200

# These should return a 302 as they should not allow the access and redirect to index if the user is not logged in:
def test_project_view_page():
    assert app.test_client().get('/projectview').status_code == 302

def test_developer_view_page():
    assert app.test_client().get('/developerview').status_code == 302

def test_add_project_page():
    assert app.test_client().get('/addproject').status_code == 302

def test_add_developer_page():
    assert app.test_client().get('/adddeveloper').status_code == 302

def test_user_management_page():
    assert app.test_client().get('/user_management').status_code == 302

def test_edit_project_page():
    assert app.test_client().get('/edit_project/1').status_code == 302

def test_edit_developer_page():
    assert app.test_client().get('/edit_developer/1').status_code == 302

def test_edit_user_page():
    assert app.test_client().get('/edit_user/1').status_code == 302

# These should now return a 200 as they should work for regular logged in users:
@pytest.fixture
def regular_user_client_success():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with client.session_transaction() as sess:
            sess['user_id'] = 1
            sess['user_name'] = 'Test User'
            sess['is_admin'] = False
        yield client

def test_project_view_logged_in(regular_user_client_success):
    assert regular_user_client_success.get('/projectview').status_code == 200

def test_developer_view_logged_in(regular_user_client_success):
    assert regular_user_client_success.get('/developerview').status_code == 200

# These should still return a 302 as they should not allow the access and redirect to index if the user is not an admin:
@pytest.fixture
def regular_user_client_failure():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with client.session_transaction() as sess:
            sess['user_id'] = 1
            sess['user_name'] = 'Test User'
            sess['is_admin'] = False
        yield client

def test_add_project_page(regular_user_client_failure):
    assert regular_user_client_failure.get('/addproject').status_code == 302

def test_add_developer_page(regular_user_client_failure):
    assert regular_user_client_failure.get('/adddeveloper').status_code == 302

def test_user_management_page(regular_user_client_failure):
    assert regular_user_client_failure.get('/user_management').status_code == 302

def test_edit_project_page(regular_user_client_failure):
    assert regular_user_client_failure.get('/edit_project/1').status_code == 302

def test_edit_developer_page(regular_user_client_failure):
    assert regular_user_client_failure.get('/edit_developer/1').status_code == 302

def test_edit_user_page(regular_user_client_failure):
    assert regular_user_client_failure.get('/edit_user/1').status_code == 302


# These should now return a 200 as they should work for admin logged in users:
@pytest.fixture
def admin_client_success():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with client.session_transaction() as sess:
            sess['user_id'] = 1
            sess['user_name'] = 'Test User'
            sess['is_admin'] = True
        yield client

def test_add_project_page(admin_client_success):
    assert admin_client_success.get('/addproject').status_code == 200

def test_add_developer_page(admin_client_success):
    assert admin_client_success.get('/adddeveloper').status_code == 200

def test_user_management_page(admin_client_success):
    assert admin_client_success.get('/user_management').status_code == 200

def test_edit_project_page(admin_client_success):
    assert admin_client_success.get('/edit_project/1').status_code == 200

def test_edit_developer_page(admin_client_success):
    assert admin_client_success.get('/edit_developer/1').status_code == 200

def test_edit_user_page(admin_client_success):
    assert admin_client_success.get('/edit_user/1').status_code == 200