#test/test_endpoints.py

import pytest
from flask import url_for
from src.manage import app  # Assuming manage.py sets up the Flask app instance

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert b'List of users' in response.data  # Adjust according to your expected response content

def test_create_user(client):
    data = {
        'username': 'testuser',
        'email': 'testuser@example.com'
    }
    response = client.post('/users', json=data)
    assert response.status_code == 201  # Assuming 201 for successful creation
    assert b'User created' in response.data  # Adjust according to your expected response content

def test_get_user_by_id(client):
    response = client.get('/users/1')  # Assuming user ID 1 exists in your database
    assert response.status_code == 200
    assert b'User details' in response.data  # Adjust according to your expected response content

def test_update_user(client):
    user_id = 1  # Assuming user ID 1 exists in your database
    data = {
        'username': 'updated_user',
        'email': 'updated_user@example.com'
    }
    response = client.put(f'/users/{user_id}', json=data)
    assert response.status_code == 200
    assert b'User updated' in response.data  # Adjust according to your expected response content

def test_delete_user(client):
    user_id = 1  # Assuming user ID 1 exists in your database
    response = client.delete(f'/users/{user_id}')
    assert response.status_code == 200
    assert b'User deleted' in response.data  # Adjust according to your expected response content

def test_create_user_missing_data(client):
    data = {
        'email': 'testuser@example.com'  # Missing 'username'
    }
    response = client.post('/users', json=data)
    assert response.status_code == 400  # Assuming 400 for bad request due to missing data
    assert b'Missing required data' in response.data  # Adjust according to your expected error message

def test_get_nonexistent_user(client):
    response = client.get('/users/999')  # Assuming user ID 999 does not exist
    assert response.status_code == 404
    assert b'User not found' in response.data  # Adjust according to your expected error message
