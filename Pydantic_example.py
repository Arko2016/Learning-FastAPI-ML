from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

'''
Field + Annotated functions help in 3 ways:
1. specify data type
2. provide default values
3. provide details about the attribute
'''

#create a Pydantic model using BaseModel to define the required variables
class Patient(BaseModel):
    name: str = Annotated[str, Field(max_length=50, title = 'Name of the patient', description='Give name of patient in less than 50 characters', examples=['ajh','ms'])] #sets contraint on string length
    age: int = Field(gt = 0, lt = 100) #age has to be within range of 0 to 120
    email: EmailStr #this is a Pydantic datatype format to help validate emails
    linkedin_url: AnyUrl #Pydantic datatype to validate links
    weight: Annotated[float, Field(gt = 0, strict=True)] #helps to set constraints, in this case indicates weight cannot be less than 0. strict ensures data type coercion does not occur
    married: Annotated[bool, Field(default=None, description="Is the patient married? enter True or False")] #a default value can be specified
    #make the allergies variable optional
    allergies: Annotated[Optional[List[str]], Field(default = None, max_length = 5)] #an optional variable should always be given a default value of None
    contact_details: Dict[str,str] # denotes that both key and value for dictionary should be string

#define a function with the pydantic object as input parameter
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')

#create a json object to be used to instantiate the Pydantic model
patient_info = {'name': 'aj', 'age': 35,'email': 'abc@xyz.com', 'weight': 180, 'linkedin_url':'http:linkedin.com/1322', 'contact_details': {'phone':'232323'}}

#instantiate pydantic object
#Note: since the patient_info is in json format, need to unpack it
patient1 = Patient(**patient_info)
#show the oject
#allergies will be None since no instantiation value was provided and allergies was defined as an Optional attribute
print(patient1)
