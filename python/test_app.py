from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_add():
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_multiply():
    response = client.post("/multiply", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 6} 

def test_divide():
    response = client.post("/divide", json={"a": 6, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2} 