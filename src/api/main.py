from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import logging
import numpy as np

app = FastAPI(title="Loan Default Prediction API")

# Load model
model = joblib.load('models/classifier_model.pkl')

class LoanRequest(BaseModel):
    Gender: int  # 1=Male, 0=Female
    Married: int  # 1=Yes, 0=No
    Dependents: int  # 0-4
    Education: int  # 1=Graduate, 0=Not Graduate
    Self_Employed: int  # 1=Yes, 0=No
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float  # Will be divided by 10 as per notebook
    Credit_History: float  # 1=Good, 0=Bad
    Property_Area: int  # 0=Rural, 1=Semiurban, 2=Urban

@app.post("/predict")
async def predict(request: LoanRequest):
    try:
        # Transform input to match model features
        features = [[
            request.Gender,
            request.Married,
            request.Dependents,
            request.Education,
            request.Self_Employed,
            request.ApplicantIncome,
            request.CoapplicantIncome,
            request.LoanAmount,
            request.Loan_Amount_Term / 10,  # Matching notebook preprocessing
            request.Credit_History,
            request.Property_Area
        ]]
        
        prediction = model.predict(features)[0]
        
        return {
            "loan_approval": "Y" if prediction == 1 else "N",
            "prediction_value": int(prediction)
        }
    except Exception as e:
        logging.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "healthy"}