"""
tests for main app
"""
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_read_main():
    """
    test GET /
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
