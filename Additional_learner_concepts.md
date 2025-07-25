## Types of Software Applications
1. Static -> Limited interaction between app and user. Eg. Calendar, Clock
2. Dynamic -> Frequent, intricate interactions between app and user. Eg. MS Excel, Word

## 4 types of Interactions with Dynamic Apps -> CRUD
1. Create
2. Retrieve
3. Update
4. Delete

Example in MS Excel:
1. We **create** an excel sheet and enter data
2. If we do summation of 2 cells, we **retrieve** data from the 2 cells and add them
3. We can also **update** information in a cell
4. We can **delete** data from a cell

## Website vs APP:
While an app is developed and usually referenced in the same local machine, a website is similar to an app but is created in one machine and used in another machine -> **Server vs Client**

Hence, websites can also be *Static vs Dynamic* and the website interactions can also be categorized into 4 types -> **CRUD**

*Note:* Since these interactions occur over an HTTP request, its crucial to mention the type of request -> GET, POST, PUT, PATCH, and DELETE, which correspond to CRUD (Create, Read, Update, Delete) operations

1. GET:
Used to retrieve data from a server. When a GET request is successful, the server typically returns a 200 (OK) status code. 
2. POST:
Used to send data to the server to create a new resource. A successful POST request often results in a 201 (Created) status code. 
3. PUT:
Used to update an existing resource on the server. It replaces the entire resource with the provided data. If the resource doesn't exist, it may create a new one. 
4. PATCH:
Similar to PUT, but it's used to *partially update* a resource. It only modifies the specified fields. 
5. DELETE:
Used to remove a resource from the server

## Path Parameters
Path parameters are dynamic URL components which are used to identify specific components
Example: localhost:8000/view/{path parameter}
They are specificlly useful for: Retrieve, Update and Delete operations

## Path function
Path function() in FastAPI is used to provide metadata, validation rules and documentation for path parameters in API endpoints
Eg. of data validations that can be provided:
Title, description, examples, min-length, max_length, regex, greater than equal to, etc.

## HTTP Status code
3-digit status code which is returned by web server (like FastAPI) to the client indicating status of the reponse for the client's request
They help the client (frontend browser) to understand:
- if the response was a success (usually 2xx)
- further action needs to be taken, may be a redirect (3xx)
- something is wrong (client error) -> 4xx
- error on server side (5xx)

examples:
200 -> response was successful
502 -> bad gateway, gateway with request failed to reach end
401 -> unauthorized access, need to login
404 -> resource doesnt exist

## HTTPException
It is a special built-in exception in FastAPI used to return custom HTTP error responses when something goes wrong in the API while handling requests
Thus, instead of returning generic JSON responses or crashing the server, we can highlight the exact error with:
- a proper HTTP status code (404, 502, etc.)
- a custom error message
- extra headers (*optional*)

## Query Parameters
Optional ke-value pairs appended to end of a URL, used to pass additional data to the server in a HTTP request.
They are typically used for filtering, sorting data, pagination or searching operations without altering the endpoint path itself

Ex.: /patient?city=Delhi&sort_by=age
In this API call, we are asking the response data to be filtered only for Delhi city and sort by age is ascending order. 
The '?' marks the start of query parameters, while '&' is used to separate out different query parameters

*Note*: the parameters are also *optional* and the request should also work without specifying them

**Query()** is a utility function under FastAPI to declare, validate and document Query parameters in API endpoints
It allows you to:
- set default values
- enforce validation rules
- add metadat like description, titles, example/references









