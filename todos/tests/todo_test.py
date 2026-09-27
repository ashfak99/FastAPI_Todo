from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

def test_get_all_todos():
    response = client.get("/todos")

    assert response.status_code==200