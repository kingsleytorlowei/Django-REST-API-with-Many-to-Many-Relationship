# Django-REST-API-with-Many-to-Many-Relationship

## How to Run

First of all install the dependencies by running the following command on your terminal ``` pip install -r requirements.txt ``` on your terminal. Configure the database by changing the values on the secrets.json file in the root directory by changing the "DATABASE NAME", "DATABASE USER" and "DATABASE PASSWORD" Then run the following commands ```python manage.py makemigrations``` and ```python manage.py migrate```

  

Authentication is required to gain access to the endpoints and to do that you need to run ```python manage.py createsuperuser``` on your terminal. This will ask for a username, email and password which we will later used on the login endpoint. Then finally run the application with ```python manage.py runserver 8100```.


## Description

This is the source for the Building a many to many modeled REST API with drf found here https://link.medium.com/HVXW1QZik0.

The API uses application/json content type and to gain full access you'll the username and password created earlier should be used for the Login endpoint and this will generate a JWT token which will be used as Authorization header with the word 'Token' coming before the actual token.

The two entities in the API are authors and books which are in a many to many relationship.
