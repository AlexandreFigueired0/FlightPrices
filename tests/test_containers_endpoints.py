import requests

class TestEndpoints():
    def test_visualization_endpoints(self):
        # run the coomand :curl localhost:8084/api/visualization/airlines/DL
        response = requests.get("localhost:8084/api/visualization/airlines/DL")
        print(response.json())
