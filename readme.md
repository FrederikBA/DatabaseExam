## Dependencies
```bash
conda create -n database_exam python=3.10.11 -y
conda activate database_exam
pip install -r requirements.txt
```
## Usage

### Server:
1. Navigate to /server
2. Run the server: `uvicorn main:app --reload`
3. Server URL: `http://127.0.0.1:8000`
4. Swagger API Documentation: `http://127.0.0.1:8000/docs`

### Client:
1. Navigate to /client
2. Install dependencies: `npm install`
3. Run the client: `npm start`

### Populate the database(s):
#### .env file
1. Create a .env file in the root of /server with the following:
<img width="349" alt="env" src="https://github.com/FrederikBA/DatabaseExam/assets/61831295/7ea71e71-ea53-4690-8a21-469b55698ee9">



#### SQL
1. Create database 'BockBluster'
1. Run query: queries/SQL/create_table.sql
2. In Postman run the request on POST: http://localhost:8000/populatesql

#### Neo4j
1. Create DB 'BockBluster' with password 12345678 on version 5.3.0
2. Install plugins: APOC, Graph Data Science Library, Neosemantics(n10s)
3. In Postman run the request on POST: http://localhost:8000/populategraph
4. In Postman run the request on POST: http://localhost:8000/nodesimilarity


# Project solution
We have developed an application that offers the capability to rent movies. This site provides a collection of 1000 movies, allowing users to browse, search, and access detailed information about each film. Additionally, registered users can log in and proceed to rent a movie of their choice.

The application's backend is implemented in Python, utilizing the fastAPI framework, while the frontend is developed using React. To ensure efficient functionality, we have integrated three databases: MSSQL, Neo4j, and Redis.

Our MSSQL database is primarily responsible for managing user accounts, movie loans, and orders. On the other hand, our Neo4j database houses our comprehensive movie catalog, encompassing relevant details such as actors, directors, genres, and more.

To enhance user experience and streamline the renting process, we have employed the Redis database to handle the cart feature on our website. Whenever a user wishes to rent a movie, the Redis database effectively manages their selection within the cart system.


# Schemas
### Neo4j
![neo4j](https://github.com/FrederikBA/DatabaseExam/assets/61831295/03652f66-5fab-48a2-8f80-1bf55d545eec)



### MSSQL
![DBDiagram](https://github.com/FrederikBA/DatabaseExam/assets/61831295/ef837404-1078-4ab7-9aa1-1c1756adf004)


<img width="507" alt="MSSQL" src="https://github.com/FrederikBA/DatabaseExam/assets/61831295/d061f4a3-131b-4b74-a9dc-8524d8c1120a">

