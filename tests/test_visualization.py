import pytest
from visualization import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_visualization_liveness_check(client):
    """Test the liveness check endpoint."""
    response = client.get('/api/visualization/liveness-check')
    assert response.status_code == 200
    assert response.data.decode() == 'ok'


def test_visualization_get_tickets_from_to(client):
    """Test the get tickets from departure to arrival endpoint."""
    response = client.get('/api/visualization/tickets/BOS/ATL')
    assert response.status_code == 200


def test_visualization_get_airline_details(client):
    """Test the get airline details endpoint."""
    response = client.get('/api/visualization/airlines/AA')
    assert response.status_code == 200
    assert response.json == {
        "airlineCode": "AA",
        "airlineName": "American Airlines"
    }
    