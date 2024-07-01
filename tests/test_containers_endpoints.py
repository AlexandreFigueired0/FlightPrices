import pytest
import requests

BASE_URL = "http://localhost"

@pytest.fixture
def client():
    return requests


def test_get_airline_details(client):
    response = client.get(f'{BASE_URL}:8084/api/visualization/airlines/DL')
    assert response.status_code == 200
    assert "airlineCode: DL" in response.text
    assert "airlineName: Delta" in response.text

def test_get_ranking(client):
    response = client.get(f'{BASE_URL}:8082/api/ranking/airlines_by_ticket_price')
    assert response.status_code == 200

