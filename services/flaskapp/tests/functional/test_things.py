

def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/poem' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/poem')
    assert response.status_code == 200
    assert b"Twas brillig, and the slithy toves" in response.data
