import os
import tempfile
import pytest
from app import app

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            # Initialize your database if needed
            init_register_db()
            init_admin_db()
            init_applicant_db()
            init_payment_db()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_index(client):
    response = client.get('/')
    assert b'Login' in response.data

def test_register(client):
    response = client.post('/register', data=dict(
        register_email='test1@example.com',
        register_password='test123'
    ), follow_redirects=True)
    assert b'Registration successful' in response.data

def test_login(client):
    response = client.post('/login', data=dict(
        login-email='test1@example.com',
        login-password='test123'
    ), follow_redirects=True)
    assert b'Dashboard' in response.data