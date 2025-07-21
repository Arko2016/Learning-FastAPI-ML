'''
This is a 2nd example for creating a basic api
'''

from fastapi import FastAPI, Path, HTTPException, Query
import json

#define FastAPI object
app = FastAPI()

#helper function to load data from patients json file
def load_data():
    #open json file in read format and load the data in a dataframe
    with open('patients.json', 'r') as f:
        data = json.load(f)
    
    return data

#define get request for home webpage
@app.get("/")
def func1():
    return {"message":"Patient Management System API"}

#define get request for 2nd webpage
@app.get("/about")
def func2():
    return {"message":"A fully functional API to manage patient records"}

#get patients records by involing load_data() function defined above
@app.get("/view")
def func3():
    data = load_data()
    return data

#get records for a specific patient using Path Parameter (which is a string in our json)
#in view patient function, provide path functions to provide documentations to API endpoints
#"..." indicates this is mandatory
@app.get("/patient/{patient_id}")
def view_patient(patient_id : str = Path(..., description = "ID of the patient in the database", example = 'P001')):
    #load patients json containing all records
    #Note: patients data is in json format with patient id as key
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    
    #return a generic Json error message
    #return {'error':'patient id not found'}

    #instead of above, we can use HTTPException to return a specific HTTP status code
    return HTTPException(status_code = 404, detail= f'Patient with ID {patient_id} not found' )

#sort patient records by a specified field in a specified order
@app.get("/sort")
#note: below which sort_by is a reqirement Path parameter, as indicated by "...", order is an optional path parameter
def sort_patients(sort_by: str = Query(..., description= 'sort on basis of height, weight, bmi'), order: str = Query('asc', description= 'sort by asc/desc order')):
    
    #specify fields for sorting
    valid_fields_sort = ['height','weight','bmi']
    
    #check if sorting attribute is among the valid fields mentioned above
    if sort_by not in valid_fields_sort:
        raise HTTPException(status_code=400, detail= f'Invalid field mentioned, please select from {valid_fields_sort}')
    
    #check if sorting order is among asc/desc
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail= 'Invalid sorting order, select within asc or desc')
    
    #load all records
    data = load_data()

    #sort data
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse = sort_order)

    return sorted_data

#filter data for based on specified condition
@app.get("/filter")
def filter_patients(filter_by : str = Query(..., description='filter and display only those patient records based on specified values for city or gender'), filter_value : str = Query(..., description= 'for city, select from (mumbai, kolkata, guwahati, pune). for gender, select from (male,female)')):

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
    #convert values in city and gender columns to lowercase for comparison


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


    






