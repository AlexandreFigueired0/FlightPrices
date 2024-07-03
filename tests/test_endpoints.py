import requests

def test_visualization_airlines_endpoint():
    response = requests.get("http://localhost:8084/api/visualization/airlines/DL")
    assert response.status_code == 200
    assert response.json() == {"airlineCode": "DL", "airlineName": "Delta"}


def test_forecaste_cheapest_endpoint():
    response = requests.get("http://localhost:8080/api/forecast/chepeast/BOS/ATL/2022-01-01/2022-01-10")
    assert response.status_code == 200
    assert response.json() == {"price": 365.12496559118614}