
import pytest
import requests

def test_get_user():
    response = requests.get('https://jsonplaceholder.typicode.com/users/2')
    assert response.status_code == 200
    assert 'id' in response.json()
    assert 'name' in response.json()
    assert 'username' in response.json()
    assert 'email' in response.json()

def test_get_nonexistent_user():
    response = requests.get('https://jsonplaceholder.typicode.com/users/999')
    assert response.status_code == 404
    assert response.json() == {}

def test_get_user_fields():
    response = requests.get('https://jsonplaceholder.typicode.com/users/2')
    user_fields = ['id', 'name', 'username', 'email']
    for field in user_fields:
        assert field in response.json()

def test_get_user_status_code():
    response = requests.get('https://jsonplaceholder.typicode.com/users/2')
    assert response.status_code == 200

def test_get_nonexistent_user_status_code():
    response = requests.get('https://jsonplaceholder.typicode.com/users/999')
    assert response.status_code == 404
