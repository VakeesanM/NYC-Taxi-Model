from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_prediction():
    payload = {
        "Trip_Distance_km": 10.5,
        "Time_of_Day": "Morning",
        "Day_of_Week": "Monday",
        "Passenger_Count": 2,
        "Traffic_Conditions": "Low",
        "Weather": "Clear",
        "Base_Fare": 3.0,
        "Per_Km_Rate": 1.2,
        "Per_Minute_Rate": 0.5,
        "Trip_Duration_Minutes": 15.0
    }
    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert isinstance(response.json()["prediction"], float)