FROM python:3.11-slim


WORKDIR NYC Taxi Price Prediction/Model Deployment

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

Expose 8000

cmd ["uvicorn", 'main:app', "--host", "0.0.0.0", "--port", "8000"]