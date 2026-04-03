# Tests name input validation
import pytest
from app import sanitise_name 

# Test valid name examples:
def test_valid_names():
    names = [
        "Bob",
        "Bob Jones",
        "Mary-Jane",
        "Nic Nic",
        "Fred O'Connor"
    ]
    for name in names:
        assert sanitise_name(name) == name

# Test invalid name examples:
def test_invalid_names():
    names = [
        "Bob123",     
        "Bob!",         
        "Mary_Jane",    
        "Nic!Nic",   
        "Fred O'Connor@@@"   
    ]
    for name in names:
        with pytest.raises(ValueError):
            sanitise_name(name)

         