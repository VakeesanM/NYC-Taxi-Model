# NYC Taxi Price Precition API with Sklearn Project

This is a sklearn model that predicts the prices of Taxi rides in NYC for my resume, that deploys a constantly updating API, found at:
https://taxi-price-prediction-pipeline-api.onrender.com/


This project has the following steps:
1. Data Cleaning of Dataset with errors and missing values
2. Sklearn Pipeline with encoding, scaling, feature creation and selection
3. Model Conversation into API via Fastapi
4. Dockerization of API with Docker 
5. CI/CD using Github Actions.

### How to use

This API takes in a JSON body and returns a prediction. The JSON Body must contain the following fields to predict price.

| Feature               | Data Type | Description  |
| --------------------- | --------- | - |
| Trip_Distance_km      | float     |   |
| Time_of_Day           | str       | Morning, Afternoon, Evening, or Night |
| Day_of_Week           | str       |  Weekend or Weekday |
| Passenger_Count       | int       |   |
| Traffic_Conditions    | str       | Low, Medium or High  |
| Weather               | str       | Clear, Rain or Snow |
| Base_Fare             | float     |   |
| Per_Km_Rate           | float     |   |
| Per_Minute_Rate       | float     |   |
| Trip_Duration_Minutes | int       |   |

The categorical Values are case sensetive and must be entered as shows above. 