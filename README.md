# Rest API for ACME Company
This project is designed to help the ACME Company have an API, that could manage the store, register, and creating with information like an address. Also is possible to register items for sale for each store and even proceed with simple order (No payment).

### Documentation of usage of the API:
The documentation was designed using the principles of Swagger and written on its version OpenAPI 3.1.

Open the [***openapi.yaml***](https://github.com/tonykingnz/hugapi-acme-api/blob/development/openapi.yaml) file on your swagger viewer of preference, or simply copy and past it text onto https://editor.swagger.io/ and see the documentation at the right side (Take care to don't change accidentally the code of the left side that you pasted from the file  [***openapi.yaml***](https://github.com/tonykingnz/hugapi-acme-api/blob/development/openapi.yaml)).

You can copy the ***cURL command*** generate after using the *Try it out* button and paste in the terminal to contact the API.

Example for the Order:

    curl -X POST "http://localhost:8000/stores/0/orders" -H  "accept: application/json" -H  "Content-Type: application/json" -d " {\"storeOrderId\":0,\"customerId\":0,\"confirmationDate\":\"2004-10-19 10:23:54+02\",\"status\":\"pending\",\"item\":{\"storeItemPricingId\":10.89,\"quantity\":0.12,\"unit\":\"kg\"}}"
    

### Install:
#### Without docker on the terminal (Not recommended, skip to docker):

You must have the Python lastest version installed (The lastest version tested is Python 3.8.6) and run all the following commands:

> apt-get update

> apt upgrade

> apt-get install postgresql -y

> pip install --upgrade pip

> pip3 install hug -U 

> pip install psycopg2

> pip install swagger-ui-bundle

> pip install openapi-spec-validator

Then do all commands in the run section of Docker instructions (Maybe be slightly different to use the database, take care and go at your own risk).

#### Installation using Docker:

You can simply run the docker image with docker-compose (make sure [Docker](https://www.docker.com) is installed):

> docker-compose up -d

and then run the following command to enter inside the workspace system, with all dependencies:

> docker exec -it **your_workspacename (** docker ps **and find the workspace name)** ./bin/bash

Maybe ***hug-acme-api-store_hugapi_workspace_1***

The project folder is inside ˜/root

> cd root/

##### Run:
Login into the database with ***pslq***:

> psql -h hug-acme-api-store_acme-db-postgres_1 --port 5432 -d acme-db -U postgres -W

*password and user*: **Postgres** 
*name*: **acme-db** 
*host*: the postgres container runining in docker (Check with docker ps the **postgres docker container** as did with the workspace [Maybe ***hug-acme-api-store_acme-db-postgres_1***])
*port*: **5432**

> \e migrate.sql

Then exit with \q and run:

> hug -f app.py

The server will be up in port 8000 of the localhost (http://localhost:8000/)

### Built With

* [Hug - Embrace the APIs of the future](http://hug.rest/)
* [PostgresSQL](https://www.postgresql.org)
* [Docker](https://www.docker.com)
* [OpenAPI 3.1 (Swagger)](https://swagger.io)

###### last updated: 2020-11-05 13:18:50 (UTC -3)
