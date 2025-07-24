from pydantic import BaseModel, EmailStr,computed_field
from typing import List, Dict

'''
computed fields help to dynamically create computed field based on specified pydantic objects
'''

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float # kg
    height: float # mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calc_bmi(self) -> float: #indicates the calculated bmi field will be of tyoe float
        bmi = round(self.weight/(self.height ** 2),2)
        return bmi 
    
def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI', patient.calc_bmi) #Note: here the computed field function itself becomes the pydantic model object
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'height': 1.72, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

patient1 = Patient(**patient_info)
update_patient_data(patient1)
