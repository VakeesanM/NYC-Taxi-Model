import joblib
import sklearn
import pandas as pd

model = joblib.load("taxi_model_V1.0.0.pkl")


def predict(values: dict):
    input_data = pd.DataFrame([values])
    return round(model.predict(input_data).item(),2)



values = {
    "Trip_Distance_km": 19.35,
    "Time_of_Day": "Morning",
    "Day_of_Week": "Weekday",
    "Passenger_Count": 3,
    "Traffic_Conditions": "Low" ,
    "Weather": "Clear",
    "Base_Fare": 3.56,
    "Per_Km_Rate": 0.8,
    "Per_Minute_Rate": 0.32, 
    "Trip_Duration_Minutes": 53.82
    }
print(predict(values))