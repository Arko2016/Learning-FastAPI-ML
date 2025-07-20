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

wip
