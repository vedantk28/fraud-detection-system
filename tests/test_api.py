from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_predict_endpoint():
    transaction = {"src": "A", "dst": "B", "amount": 100}
    response = client.post("/predict", json=transaction)

    assert response.status_code == 200
    data = response.json()
    assert "fraud_prediction" in data
    assert isinstance(data["fraud_prediction"], int)
