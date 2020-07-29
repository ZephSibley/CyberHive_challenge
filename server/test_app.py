from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_post_main():
    response = client.post(
        '/',
        json={
            'running_processes': ['process one', 'process two'],
            'timestamp': '29/07/2020 18:00'
        }
    )
    assert response.status_code == 200


def test_bad_payload():
    response = client.post(
        '/',
        json={
            'junk': 'string'
        }
    )
    assert response.status_code == 422


def test_no_timestamp():
    response = client.post(
        '/',
        json={
            'running_processes': ['process one', 'process two'],
            'timestamp': None
        }
    )
    assert response.status_code == 422


def test_no_processes():
    response = client.post(
        '/',
        json={
            'running_processes': None,
            'timestamp': '29/07/2020 18:00'
        }
    )
    assert response.status_code == 422
