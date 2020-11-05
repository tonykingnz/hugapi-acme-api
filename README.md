# Rest API for ACME Company
This project is designed to help the ACME Company have an API, that could manange they store, registring and creating with information like address. Also is possible to registre items for sale for each store an even procede with simple order (No payment).

### Documentation of usage of the API:
The documentation was desing using the principes of Swagger and writen on it version OpenAPI 3.1.

Open the ***openapi.yaml*** file on your swagger viewer of preference, or simple copy and past it text onto https://editor.swagger.io/ and see the documentation at the right side.

You can copy the cURL coomand generate after usig the Try button, and paste in the terminal to contact the API.

### Install:
#### Witout docker on terminal (Not recomended, skip to docker):

You must have the python lastest version installed (Lastest version tested is Python 3.8.6), and run all the following commands:

> apt-get update

> apt upgrade

> apt-get install postgresql -y

> pip install --upgrade pip

> pip3 install hug -U 

> pip install psycopg2

> pip install swagger-ui-bundle

> pip install openapi-spec-validator

Then do all commnands in run section of Docker instructions (Maybe be slight diferent to use database, take care and go at your own risk).

#### Installation using Docker:

You can simple run the docker image with docker-compose:

> docker-compose up -d

and then run the following command to enter inside the workspace system, with all dependencies:

> docker exec -it **your_workspacename (** docker ps **and find the workspace name)** ./bin/bash

Maybe ***hug-acme-api-store_hugapi_workspace_1***

The project folder is inside ˜/root

> cd root/

##### Run:
Login into the database with ***pslq***:

> psql -h hug-acme-api-store_acme-db-postgres_1 --port 5432 -d acme-db -U postgres -W

*password and user*: **postgres** 
*name*: **acme-db** 
*host*: the postgres container runining in docker (Check with docker ps the **postgres docker container** as did with the workspace [Maybe ***hug-acme-api-store_acme-db-postgres_1***])
*port*: **5432**

> \e migrate.sql

Then exit with \q and run:

> hug -f app.py

The server will be up in the port 8000 of the localhost (http://localhost:8000/)

### Demo Image of the Swagger UI:
If not displaying, open the file: [SwaggerUI.pdf](https://github.com/tonykingnz/RestAPIACMECompany/blob/master/SwaggerUI.pdf)

![Swagger UI Demo Image](SwaggerUI.pdf)

### Built With

* [Hug - Embrace the APIs of the future](http://hug.rest/)
* [PostgresSQL](https://www.postgresql.org)
* [OpenAPI 3.1 (Swagger)](https://swagger.io)

###### last updated: 2020-11-05 12:17:50 (UTC -3)
