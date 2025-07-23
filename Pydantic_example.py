from pydantic import BaseModel
from typing import List, Dict, Optional

#create a Pydantic model using BaseModel to define the required variables
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool = False #a default value can be specified
    #make the allergies variable optional
    allergies: Optional[List[str]] = None #an optional variable should always be given a default value of None
    contact_details: Dict[str,str] # denotes that both key and value for dictionary should be string

#define a function with the pydantic object as input parameter
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')

#create a json object to be used to instantiate the Pydantic model
patient_info = {'name': 'aj', 'age': 35, 'weight': 180, 'contact_details': {'phone':'232323'}}

#instantiate pydantic object
#Note: since the patient_info is in json format, need to unpack it
patient1 = Patient(**patient_info)
#show the oject
#allergies will be None since no instantiation value was provided and allergies was defined as an Optional attribute
print(patient1)
