## What is Pydantic?
Pydantic is a Python library that allows you to define data models and validate data at runtime using Python type hints

## Main advantages of Pydantic
1. Data Type validation: If the required format of inpit data needs to be integer, but the user enters string, pydantic helps formatting the same
2. Data Constraint validation: If the entered data cannot be -ve, but the user inputs a -ve value, Pydantic is able to validate the same
3. Data Parsing and Conversion: Pydantic can convert input data into the appropriate Python types, such as automatically parsing JSON strings into Python objects that adhere to your defined schema
4. Error Handling: When validation fails, Pydantic provides detailed and informative error messages, making it easier to pinpoint issues in your input data

