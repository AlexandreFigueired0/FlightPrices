import pytest
from ranking import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_ranking_liveness_check(client):
    """Test the liveness check endpoint."""
    response = client.get('/api/ranking/liveness-check')
    assert response.status_code == 200
    assert response.data.decode() == 'ok'

    