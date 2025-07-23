## What is Pydantic?
Pydantic is a Python library that allows you to define data models and validate data at runtime using Python type hints

## Main advantages of Pydantic
1. Data Type validation: If the required format of inpit data needs to be integer, but the user enters string, pydantic helps formatting the same
2. Data Constraint validation: If the entered data cannot be -ve, but the user inputs a -ve value, Pydantic is able to validate the same
3. Data Parsing and Conversion: Pydantic can convert input data into the appropriate Python types, such as automatically parsing JSON strings into Python objects that adhere to your defined schema
4. Error Handling: When validation fails, Pydantic provides detailed and informative error messages, making it easier to pinpoint issues in your input data

## How does Pydantic function?
1. Define a Pydantic model/class that represents idea schema of the data
    - Mention the expected fields, their data types and any validation constraints (eg. data cannot be -ve)
2. Create an example raw input data (which is usually a dictionary or json format) to Instantiate the model
    - Pydantic will automatiaclly validate the data and coerce it into Python data types, else raise a *Validation Error*
3. Pass the validated model object to functions or throughout the codebase
    - ensures every part of the program work with clean, type-safe, logically valid data

