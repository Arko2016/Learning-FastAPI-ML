## How are applications built without using API?
Without using API, all the software components become tightly-coupled which can cause several problems
<img width="540" height="476" alt="monolithic architecture pic1 drawio" src="https://github.com/user-attachments/assets/523e9f1e-37e4-4fcd-b84c-649ed315c093" />


## Use case:
Let's consider there is a government travel agency with a central database which contains data about all trains, timings and detsinations. Now let's say, we have 3rd part websites wants to leverage this database for serving customers visiting their website and pay the gov. agency a share everytime the data is used.

If the agency only wants to share Backend information with 3rd party websites without providing them access to the database, because of the tightly coupled architecture, it will have to provide access to the entire database or else miss out on the monetisation opportunity.Therefore, it becomes difficult to share data securely with any external client

### Disadvantages of Monolithic Architecture:
1. Scalability Challenges:
Can only scale the entire application, even if only a small part requires more resources. This leads to inefficient resource utilization. Also, if one module experiences high traffic, the entire application needs to be scaled 
2. Slower Development Speed:
Integrating new technologies into a monolithic application or even small code changes require redeploying the entire application. Also, a bug in any module can potentially bring down the entire application
3. Deployment Issues:
Frequent deployments are challenging due to the need to redeploy the entire application

### API (Application Programming Interface)
<img width="725" height="510" alt="api pic 1 drawio" src="https://github.com/user-attachments/assets/d1cd3efe-2f75-4d4c-bfad-0d5fb594acee" />

Decoupling the backend from frontend allows the governing body to set multiple constraints which can prevent unwanted use or corruption of backend from external applications

APIs are mechanisms that enable 2 software components, such as Frontend and Backend of an application, to communicate with each other using set of rules, protocols and data formats

<img width="563" height="234" alt="api pic 2 drawio" src="https://github.com/user-attachments/assets/2c179f02-d989-4d2a-b605-8216c1ab9c29" />

*NOTE:* While client sends data to API through HTTP requests, the final output from API as it returns response is in the form of json files so that it can be interpreted by any frontend application code (Python, JAVA, PHP, etc.)

## Analogy to Remember API architecture:
In a restaurant, a **customer** looks at the menu and decides what to order -> **Frontend**
The waiter receives the order and mentions to chef, who then prepares the food using required ingredients and the waiter then delivers the food back to customer
    In this case, **Waiter -> API, Ingredients -> Database, Chef -> Backend**
In **Synchronous architecture**, once 1 order is placed, the waiter waits till the processed food is delivered before accepting another order. However in **Asynchronous archotecture**, while the food is getting prepared for 1 order, the waiter can receive request for other orders, thus **serving multiple customers** at the same time




