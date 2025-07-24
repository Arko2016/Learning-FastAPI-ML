from pydantic import BaseModel

'''
nested models helps to reference one Pydatic object within another
'''

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str = 'Male'
    age: int
    address: Address #here address is defined using another pydantic object

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'gender': 'male', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

#Now we can export the above model both as dictionary and json
#dictionary
temp_dict1 = patient1.model_dump(include = {'name','age', 'address'})
#Note: exclude works in reverse method as above
print(temp_dict1)
print(type(temp_dict1))

temp_dict2 = patient1.model_dump(include = {'address':['city']})
#Note: we can only include either names of the keys or specific values within a key, not both combinations
print(temp_dict2)
print(type(temp_dict2))

#json
temp_json = patient1.model_dump_json()
print(temp_json)
print(type(temp_json))

'''
exclude_unset = True => if an attribute is not explicity defined during object creation, even if it had been set a default value during pydantic model defination, it will be nt be included during model export to json or dictionary
'''
patient_dict2 = {'name': 'nitish', 'age': 35, 'address': address1}

patient2 = Patient(**patient_dict2)
temp_dict3 = patient2.model_dump(exclude_unset=True)
#Note: here since gender was not set during patient2 creation, even though a default value was set during pydantic model/class instantiation, this will not be included
print(temp_dict3)
print(type(temp_dict3))


