import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Test that the index page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Very nice deploy" in response.data

def test_about_page(client):
    """Test that the about page loads successfully."""
    response = client.get('/about')
    assert response.status_code == 200
    assert b"This is the about page" in response.data
