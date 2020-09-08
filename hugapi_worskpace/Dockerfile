FROM python:buster

RUN apt-get update
RUN apt upgrade

RUN apt install git
RUN apt install vim -y
RUN apt-get install postgresql -y

RUN pip install --upgrade pip

RUN pip3 install hug -U 
RUN pip install psycopg2
RUN pip install swagger-ui-bundle
RUN pip install openapi-spec-validator

CMD vim
 
