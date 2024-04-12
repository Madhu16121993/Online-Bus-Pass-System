import os
import tempfile
import pytest
from app import app, init_register_db, init_admin_db, init_applicant_db, init_payment_db

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

def test_login(client):
    # Replace 'existing_username' and 'existing_password' with actual credentials
    response = client.post('/login', data={
        "login_email": "156@gmail.com",
        "login_password": "156"
    }, follow_redirects=True)
    assert b'Dashboard' in response.data
