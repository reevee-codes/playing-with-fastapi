from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_read_root():
    payload = {
        "pierwszy": 2,
        "drugi": 2
    }
    response = client.post("/dodaj", json=payload)
    assert response.status_code == 200
    assert response.json() == {"wynik": 4}