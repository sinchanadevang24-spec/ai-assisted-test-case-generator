
import pytest

def login(email, password):
    # placeholder function for testing
    if email == "test@example.com" and password == "password123":
        return True
    else:
        return False

def test_valid_login():
    email = "test@example.com"
    password = "password123"
    assert login(email, password) == True

def test_wrong_password():
    email = "test@example.com"
    password = "wrongpassword"
    assert login(email, password) == False

def test_empty_email():
    email = ""
    password = "password123"
    assert login(email, password) == False

def test_empty_password():
    email = "test@example.com"
    password = ""
    assert login(email, password) == False

def test_invalid_email():
    email = "invalid"
    password = "password123"
    assert login(email, password) == False
