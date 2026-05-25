from fastapi import FastAPI, Path
from pydantic import BaseModel
from App.Model import predict

class Prediction(BaseModel):
    Trip_Distance_km: float
    Time_of_Day: str
    Day_of_Week: str
    Passenger_Count: int 
    Traffic_Conditions: str
    Weather: str
    Base_Fare: float
    Per_Km_Rate: float
    Per_Minute_Rate: float
    Trip_Duration_Minutes: float 



app = FastAPI()


@app.post("/predict")
def prediction(case:Prediction):
    result = predict(case.model_dump())
    return {"prediction": result}