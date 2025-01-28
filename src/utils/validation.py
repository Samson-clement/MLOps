import pandas as pd

def validate_input_data(data: dict) -> bool:
    """Validate input data matches expected format and ranges"""
    try:
        # Check value ranges
        if data['Gender'] not in [0, 1]:
            return False
        if data['Married'] not in [0, 1]:
            return False
        if not 0 <= data['Dependents'] <= 4:
            return False
        if data['Education'] not in [0, 1]:
            return False
        if data['Self_Employed'] not in [0, 1]:
            return False
        if data['Property_Area'] not in [0, 1, 2]:
            return False
        if not 0 <= data['Credit_History'] <= 1:
            return False
        
        return True
    except KeyError:
        return False