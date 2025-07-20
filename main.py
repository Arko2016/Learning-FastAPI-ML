'''
Need to install libraries uvicorn, pydantic, fastapi[standard]
'''

from fastapi import FastAPI

#define FastAPI object
app = FastAPI()

#define get request for home webpage
@app.get("/")
def func1():
    return {"message":"hello world, this is first test webpage"}

#define get request for 2nd webpage
@app.get("/about")
def func2():
    return {"message":"this is the second test webpage"}

'''
we need to execute the code to launch API usining uvicorn using below command:
uvicorn main<which is the name of the file>:app <the FastAPI object> --reload (this will help to
refresh the webpage automatically after edits)

Additionally, if we want to access the dynamic docs for each of the app functions defined, 
just go to:
http://127.0.0.1:8000(the port in which API is launched)/docs

'''