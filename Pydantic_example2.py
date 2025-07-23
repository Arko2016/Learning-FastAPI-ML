from pydantic import BaseModel, EmailStr, field_validator


'''
field_validator can help in several ways:
1. to check if a string contains a valid substring, if email is from icici.com domain
2. to transform a variable, eg. convert name to uppercase
3. check if the varibale is within a specific range
Note: the 'mode' parameter in field validator specifies whether validation will be performed on coerced variable or the original format
field validator is defined within the pydantic model class
'''

#define pytdantic model
class Patient(BaseModel):
    name:str
    age:int
    email:EmailStr

    #field validator to check if a string contains a valid substring
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        #here, value is the email entered by user
        valid_email_domains = ['hdfc.com','icici.com']
        email_domain = value.split('@')[-1]
        if email_domain not in valid_email_domains:
            raise ValueError("Not valid email address")
        
        return value

    #field validator to transform a variable
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

    #field validator check if the varibale is within a specific range as well as function of mode parameter
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        #Note, because the mode is set as 'after', which is also default value, the value or age in below format will be the transformed value even if age is initiate with a number in string format
        if 0<value<100:
            return value
        else:
            raise ValueError('age should be between 0 and 100')

#define function to update patient records
def update_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)

#define json to instantiate pydantic model
patient_info = {'name':'aj', 'age':'30', 'email':'xyz@hdfc.com' }

patient1 = Patient(**patient_info)
update_patient(patient1)
