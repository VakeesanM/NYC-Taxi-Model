import joblib
import sklearn
import pandas as pd
import os

Base_dir = os.path.dirname(__file__)
model_path = os.path.join(Base_dir, "taxi_model_V1.0.0.pkl")
model = joblib.load(model_path)


def predict(values: dict):
    input_data = pd.DataFrame([values])
    return round(model.predict(input_data).item(),2)
