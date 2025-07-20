## What is FastAPI?
Modern, high-performance web framework for building APIs with Python. 
It's primarily built on top of 2 Python libraries:
1. **Starlette:** Manages how the API receives requests and sends back responses
2. **Pydantic:** Used to check the data coming into the API and in the right format


## USP of FastAPI:
1. **Fast to Run**
 
<img width="642" height="812" alt="fastapi pic 1" src="https://github.com/user-attachments/assets/f222d7e0-98b9-427b-b511-1db7c4b22c89" />

*Note:* SGI : Synchronous Gateway Interface, ASGI: Asynchronous Gateway Interface
While web server accepts incoming requests from client, API code helps to process the data from backend and database 
SGI/ASGI acts as bridge which converts the HTTP requests to a json format which can be read by API code

Since FastAPI is Asynchronous, it significantly enhances performance and scalability for web applications, particularly those handling many concurrent requests or I/O-bound operations. This approach allows applications to handle a higher volume of requests without blocking, leading to faster response times and improved resource utilization

2. **Fast to Code**
    - Automatic Input validation -> through Pydantic
    - Auto-generated interactive documentation
    - Seamless integration with modern MLOps/DevOps ecosystem (Docker, Kubernetes, ML libraries)
