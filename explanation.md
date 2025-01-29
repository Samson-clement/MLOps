This codebase is a proof of concept (PoC) for implementing MLOps best practices in a loan default prediction project. The project structure includes various components necessary for developing, deploying, and maintaining a machine learning model in a production environment. Here is an overview of the key components:

1. **Data Version Control (DVC)**:
   - The project uses DVC for versioning data and models. The `.dvc/` directory contains configuration files and cache for DVC.
   - The `data/` directory contains raw and processed data.
   - The `models/` directory contains the trained model files and their DVC tracking files.

2. **Source Code**:
   - The `src/` directory contains the source code for the project, including API implementation, monitoring, and utility functions.
   - The `tests/` directory contains unit tests for the project.

3. **Notebooks**:
   - The `notebooks/` directory contains Jupyter notebooks used for exploratory data analysis and model development.

4. **Documentation**:
   - The `README.md` file provides an overview of the project, setup instructions, and details about the input features and version control.

5. **Environment and Dependencies**:
   - The `requirements.txt` file lists the Python dependencies required for the project.
   - The `venv` directory contains the virtual environment for the project.

6. **Containerization**:
   - The `Dockerfile` and `docker-compose.yml` files are used for containerizing the application using Docker.

7. **Logs**:
   - The `logs/` directory is used to store log files generated during the execution of the application.

8. **GitHub Actions**:
   - The `.github/workflows/` directory contains configuration files for GitHub Actions, which can be used to set up CI/CD pipelines.

### Input Features Explanation

The input features for the loan default prediction model are explained in the `README.md` file:

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

The project uses both Git and DVC for version control:
- **Git**: For code version control
- **DVC**: For model and data version control

DVC tracking has been initialized for:
- Training data (`data/raw/train_loan_status1.csv`)
- Model file (`models/classifier_model.pkl`)

### Current Features

- FastAPI implementation for model serving
- Basic error handling and input validation
- DVC integration for data and model versioning
- Clear project structure following MLOps best practices

### Next Steps

- Add comprehensive testing
- Set up CI/CD pipeline
- Implement model monitoring
- Add documentation using Swagger/OpenAPI
- Containerize the application using Docker
- Set up model performance monitoring

### Contributing

Contributors are encouraged to update tests and documentation as appropriate and follow the existing code style.