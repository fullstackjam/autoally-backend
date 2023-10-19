from fastapi.testclient import TestClient

from app import api

client = TestClient(api)


def test_root():
    response = client.get("/docs")
    assert response.status_code == 200
