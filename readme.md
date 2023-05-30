<h1 align="center">Client/Server with FastAPI and React</h1>
<p>
</p>

## Dependencies
```sh
pip install fastapi
```

```sh
pip install uvicorn
```

```sh
pip install pydantic
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

# Project solution
We have developed an application that offers the capability to rent movies. This site provides a collection of 1000 movies, allowing users to browse, search, and access detailed information about each film. Additionally, registered users can log in and proceed to rent a movie of their choice.

The application's backend is implemented in Python, utilizing the fastAPI framework, while the frontend is developed using React. To ensure efficient functionality, we have integrated three databases: MSSQL, Neo4j, and Redis.

Our MSSQL database is primarily responsible for managing user accounts, movie loans, and orders. On the other hand, our Neo4j database houses our comprehensive movie catalog, encompassing relevant details such as actors, directors, genres, and more.

To enhance user experience and streamline the renting process, we have employed the Redis database to handle the cart feature on our website. Whenever a user wishes to rent a movie, the Redis database effectively manages their selection within the cart system.


# Schemas
### Neo4j
![neo4j](https://github.com/FrederikBA/DatabaseExam/assets/61831295/03652f66-5fab-48a2-8f80-1bf55d545eec)



### MSSQL
<img width="507" alt="MSSQL" src="https://github.com/FrederikBA/DatabaseExam/assets/61831295/d061f4a3-131b-4b74-a9dc-8524d8c1120a">

