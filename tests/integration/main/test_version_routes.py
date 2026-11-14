"""
Integration tests for the /version route.
"""
from flask import current_app


def test_version_default(client):
    """
    Test that the default version is unknown.
    """
    with client.application.app_context():
        current_app.config['APP_VERSION'] = 'unknown'

    response = client.get('/version')

    assert response.status_code == 200
    assert response.data == b'unknown'


def test_version_set(client):
    """
    Test that the route returns a configured version.
    """
    with client.application.app_context():
        current_app.config['APP_VERSION'] = '1.0.0'

    response = client.get('/version')

    assert response.status_code == 200
    assert response.data == b'1.0.0'
