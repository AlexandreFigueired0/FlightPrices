from visualization import app as visualization_app

def test_visualization_liveness_check():
    """Test the liveness check endpoint."""
    response = visualization_app.test_client().get('/api/visualization/liveness-check')
    assert response.status_code == 200
    assert response.data.decode() == 'ok'

    