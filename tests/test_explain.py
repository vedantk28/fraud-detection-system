# tests/test_explain.py
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_explain_endpoint():
    transaction = {"amount": 100}
    response = client.post("/explain", json=transaction)
    assert response.status_code == 200
    data = response.json()
    assert "fraud_prediction" in data
    assert "explanation" in data
    assert isinstance(data["explanation"], dict)
    assert set(data["explanation"].keys()) == {"mean_amount", "total_amount", "transaction_count"}
