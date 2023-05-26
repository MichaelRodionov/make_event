# MakeEvent app
This is a simple application that allows you to create organization and start a new event
## Main features
* Authentication via django-simplejwt by email.
* Create organization.
* Create event (2 or more organizations can participate in the event).
* Search event by title.
* Filtering and ordering by date.
* LimitOffset pagination
## Technology stack   
Python v.3.10   
Poetry v.1.4.1   
Django v.3.2.0  
Django REST Framework v.3.12.0   
PostgreSQL    
Docker  
Docker-compose
## Local start  
Create local .env file with the next data:  
``` python
SECRET_KEY='your django key'
DATABASE_URL=postgres://postgres:postgres@db/make_event
DEBUG=False
```
Run API, DB and Migrations containers by:
``` python
docker-compose up --build
```
You can send requests to API by http://localhost:8000
## OpenAPI documentation
You can open API documentation by GET request to the API container:   
- localhost:8000/schema/redoc/
