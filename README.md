# Flask Pizza Api

The project demonstrate to use of [Flask]() micro framework for the creation of a an hypethoical Pizza Delivery Service API

## Features
- Use Flask with [Flask-RESTX]()
- Database integration with Flask SQLAlchemy
- Authentication with JWT
- Enviroment Seperation 
- Error handing with Werkzeug
- API documentation with SwaggerUI and Flask-RESTX
- Unit testing 
- Database Migration

## Python Packages
1. Flask
2. Flask-RESTX
3. Flask-SQLAlchemy
4. Flask-Migrate
5. Flask-JWT-Extended
6. Python-decouple
7. Pytest

## Running the project 
### Step 1:
Clone the project reposity
```
git clone https://github.com/danielogen/FlaskPizza-api.git
```
### Step 2:
Change directory to project folder, create a virtual environment and activate it

```
$ cd FlaskPizza-api
$ python -m venv env
$ source env/bin/activate
```

### Step3:
Install all the required dependencies
```
$ pip install -r requirements.txt
```
Run the project in development
```
$ export FLASK_APP=api/
$ export FLASK_DEBUG=1
$ Flask run
```
----
```
python runserver.py
```

