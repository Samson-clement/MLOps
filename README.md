# MLOps
This repository acts as a PoC for MLOps Best Practices

## Loan Default Prediction - MLOps Proof of Concept

This project demonstrates an MLOps implementation for a loan default prediction model, transforming a Jupyter notebook-based model into a production-ready application.

### Project Overview

- **Model**: Support Vector Machine (SVM) for loan default prediction
- **Input**: Customer loan application data
- **Output**: Prediction whether a loan will be approved (Y/N)

### Project Structure

```
MLOps/
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   └── main.py
├── models/
│   └── classifier_model.pkl
├── data/
│   └── raw/
│       └── train_loan_status1.csv
├── tests/
└── requirements.txt
```

### Setup Instructions

1. Create and activate virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Unix/macOS
    # or
    venv\Scripts\activate  # For Windows
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the API

Start the FastAPI server:
```bash
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
```
The API will be available at [http://localhost:8000](http://localhost:8000)

### Testing the API

You can test the API using curl:
```bash
curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{
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
}'
```

### Input Features Explanation

- **Gender**: Male (1), Female (0)
- **Married**: Yes (1), No (0)
- **Dependents**: Number of dependents (0-4)
- **Education**: Graduate (1), Not Graduate (0)
- **Self_Employed**: Yes (1), No (0)
- **ApplicantIncome**: Monthly income
- **CoapplicantIncome**: Co-applicant's monthly income
- **LoanAmount**: Loan amount in thousands
- **Loan_Amount_Term**: Term of loan in months
- **Credit_History**: Good (1), Bad (0)
- **Property_Area**: Urban (2), Semi-Urban (1), Rural (0)

### Version Control

This project uses both Git and DVC:

- **Git**: For code version control
- **DVC**: For model and data version control

DVC tracking has been initialized for:

- Training data (`data/raw/train_loan_status1.csv`)
- Model file (`models/classifier_model.pkl`)

### Current Features

- ✅ FastAPI implementation for model serving
- ✅ Basic error handling and input validation
- ✅ DVC integration for data and model versioning
- ✅ Clear project structure following MLOps best practices

### Next Steps

- Add comprehensive testing
- Set up CI/CD pipeline
- Implement model monitoring
- Add documentation using Swagger/OpenAPI
- Containerize the application using Docker
- Set up model performance monitoring

### Contributing

Please make sure to:

- Update tests as appropriate
- Update documentation for any new features
- Follow the existing code style