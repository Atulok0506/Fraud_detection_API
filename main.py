from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Define the input data model using Pydantic
class InputData(BaseModel):
    step: float
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float
    isFlaggedFraud: int
    type_CASH_IN: int
    type_CASH_OUT: int
    type_DEBIT: int
    type_PAYMENT: int
    type_TRANSFER: int

# Load the pickled Random Forest model
with open("random_forest_model.pkl", "rb") as f:
    model = joblib.load(f)

# Create a FastAPI app instance
app = FastAPI()

# Define a POST endpoint for making predictions
@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert input data to a NumPy array
        features = np.array([[data.step, data.amount, data.oldbalanceOrg, data.newbalanceOrig,
                              data.oldbalanceDest, data.newbalanceDest, data.isFlaggedFraud,
                              data.type_CASH_IN, data.type_CASH_OUT, data.type_DEBIT,
                              data.type_PAYMENT, data.type_TRANSFER]])

        # Make prediction using the loaded model
        prediction = model.predict(features)

        # Return the predicted class (0 or 1) as JSON response
        return {"prediction": int(prediction[0])}
    except Exception as e:
        # Return HTTP 500 error if prediction fails
        raise HTTPException(status_code=500, detail=str(e))

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}
