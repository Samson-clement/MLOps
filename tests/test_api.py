import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_predict_endpoint():
    test_input = {
        "Gender": 1,
        "Married": 1,
        "Dependents": 2,
        "Education": 1,
        "Self_Employed": 0,
        "ApplicantIncome": 5849,
        "CoapplicantIncome": 0,
        "LoanAmount": 128,
        "Loan_Amount_Term": 360,
        "Credit_History": 1,
        "Property_Area": 2
    }
    
    response = client.post("/predict", json=test_input)
    assert response.status_code == 200
    assert "loan_approval" in response.json()
    assert response.json()["loan_approval"] in ["Y", "N"]