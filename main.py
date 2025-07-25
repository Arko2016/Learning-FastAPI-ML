'''
This is the final app code that we will build for api
'''
from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

#define FastApi app object
app = FastAPI()

#create a Pydantic model/class
class Patient(BaseModel):
    id: Annotated[str, Field(..., description="ID of patient", examples=["P001","P002"])]
    name: Annotated[str, Field(..., description="Name of Patient")]
    city: Annotated[str, Field(...,description="City where patient lives")]
    age: Annotated[int, Field(...,gt = 0, lt = 120, description="age of patient")]
    gender: Annotated[Literal['male','female','others'], Field(...,description="identified gender of patient")]
    height: Annotated[float,Field(...,gt = 0, description="height of patient in meters")]
    weight: Annotated[float, Field(...,gt = 0,description="weight of patient in kgs")]

    #computed field to calculate bmi
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height ** 2),2)
        return bmi
    
    #computed field to provide verdict on obesity based on bmi
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obese' 
    
#function to load existing patients json data#Note: open the patients json in read(r) format
def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

#define function to save updated data in json format
#Note: open the patients json in write(w) format
def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)

#api path to load welcome page -> GET request
@app.get('/')
def hello():
    return {'message':'Patient Management System API'}

#api path to read about the website -> GET request
@app.get('/about')
def about():
    return {'message':'A fully functional api to manage patient records'}

#api path to view all patient records -> GET request
@app.get('/view')
def view():
    data = load_data()
    return data

#api path to view specific patient based on patient id -> GET request
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description = "id of patient in the Database", example = ['P001'])):
    #load all patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail = f'Patient with {patient_id} not present in records')

#api path to sort records based on selected attribute and order (asc/desc) -> GET request
@app.get('/sort')
def sort_patients(sort_by: str = Query(...,description='Sort on basis height, weight or bmi'), order_by: str = Query('asc', description="Sort by asc or desc order")):
    #specify valid fields for sorting
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail = f'{sort_by} not a valid attribute, please select from height, weight, bmi')
    
    #check if sorting order is among asc/desc
    if order_by not in ['asc','desc']:
        raise HTTPException(status_code=400, detail= 'Invalid sorting order, select within asc or desc')
    
    #load data
    data = load_data()

    sort_order = True if order_by == 'desc' else False
    #sort data based on order specified
    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse = sort_order)

    return sorted_data

#api path to filter data for based on specified condition -> GET request
@app.get("/filter")
def filter_patients(filter_by : str = Query('gender', description='filter and display only those patient records based on specified values for city or gender'), filter_value : str = Query('male', description= 'for city, select from (mumbai, kolkata, guwahati, pune). for gender, select from (male,female)')):

    #convert inputs to lower case
    filter_by = filter_by.lower()
    filter_value = filter_value.lower()

    #specify columns to filter records
    valid_fields_filter = ['city','gender']

    #check if filtering attribute is among the valid fields mentioned above
    if filter_by not in valid_fields_filter:
        raise HTTPException(status_code=400, detail = f'incorrect filtering column entered, please select between {valid_fields_filter}')
    
    #load all records
    data = load_data()
    
    #get unique values for cities and gender
    city_list = list(set(x['city'].lower() for x in data.values()))
    gender_list = list(set(x['gender'].lower() for x in data.values()))

    #filter records
    if filter_by == 'city':
        filtered_data = [x for x in data.values() if x[filter_by].lower() == filter_value.lower()]
        if len(filtered_data) == 0:
            raise HTTPException(status_code=400, detail = f'invalid filter value. select between {city_list}')
        return filtered_data
    elif filter_by == 'gender':
        filtered_data = [x for x in data.values() if x[filter_by].lower() == filter_value.lower()]
        if len(filtered_data) == 0:
            raise HTTPException(status_code=400, detail = f'invalid filter value. select between {gender_list}')
        return filtered_data
    
#api path to insert a new record, if it does not exist, to the patients registry (json) -> POST request
#the Patient record entered by used will be entered and validated as a Pydantic model
@app.post('/create')
def create_patient(patient: Patient): 

    #load existing data
    data = load_data()

    #check if entered patient record already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")
    
    #add new patient to database
    #Note: to match existing format of patients json, exclude patient id from the user input json and use it as key to include new record
    data[patient.id] = patient.model_dump(exclude=['id'])

    #save into a json file
    save_data(data)

    #return a success http response
    return JSONResponse(status_code=201, content = {'message':'new patient record successfully created'})





    



    






