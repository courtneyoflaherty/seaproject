# Tests email input validation
import pytest
from app import validate_email_address  

# Test valid email examples:
# Expected output is returning the valid email:
def test_valid_emails():
    emails = [
        "test@example.com",
        "bob.jones@gmail.com",
        "abc123@test.co.uk"
    ]
    for email in emails:
        assert validate_email_address(email) == email

# Test invalid email examples:
# Expected output is returning ValueError for each invalid email:
def test_invalid_emails():
    emails = [
        "test",
        "test@",
        "test@com",
        "test@example",
        "test@.com",
    ]
    for email in emails:
        with pytest.raises(ValueError):
            validate_email_address(email)

         