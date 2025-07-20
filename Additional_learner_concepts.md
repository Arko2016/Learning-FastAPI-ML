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





