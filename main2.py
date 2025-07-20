'''
This is a 2nd example for creating a basic api
'''

from fastapi import FastAPI
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


