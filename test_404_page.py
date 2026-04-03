# Tests 404 page
import pytest
from app import app

# Test that a non-existent URL returns a 404 code:
def test_404_page():
    client = app.test_client()
    response = client.get('/examplepageurl')
    assert response.status_code == 404

# Test that an existing URL (index) returns not a 404 code:
def test_existing_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code != 404