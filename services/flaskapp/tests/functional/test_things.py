from flask import url_for


def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/poem' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/poem')
    assert response.status_code == 200
    assert b"Twas brillig, and the slithy toves" in response.data


def test_add_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/add' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/add')
    assert response.status_code == 200
    assert b'Name' in response.data
    assert b'Description' in response.data


# def test_foo(test_client):
#     response = test_client.post(
#         '/add', data=dict(name='name', description='description'))
#     assert response.status_code != 500
