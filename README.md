# Flask Pizza Api

The project demonstrate to use of [Flask](https://flask.palletsprojects.com/en/2.2.x/) micro framework for the creation of a an hypethoical `Pizza Delivery Service API`

## Features
- Use Flask with [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/)
- Database integration with Flask SQLAlchemy
- Authentication with JWT
- Enviroment Seperation 
- Error handing with Werkzeug
- API documentation with SwaggerUI and Flask-RESTX
- Unit testing 
- Database Migration
## Routes to Implement
| Method | Route | Functionality |Access|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/auth/signup/``` | _Register new user_| _All users_|
| *POST* | ```/auth/login/``` | _Login user_|_All users_|
| *POST* | ```/orders/order/``` | _Place an order_|_All users_|
| *PUT* | ```/orders/order/update/{order_id}/``` | _Update an order_|_All users_|
| *PUT* | ```/orders/order/status/{order_id}/``` | _Update order status_|_Superuser_|
| *DELETE* | ```/orders/order/delete/{order_id}/``` | _Delete/Remove an order_ |_All users_|
| *GET* | ```/orders/user/orders/``` | _Get user's orders_|_All users_|
| *GET* | ```/orders/orders/``` | _List all orders made_|_Superuser_|
| *GET* | ```/orders/order/{order_id}/``` | _Retrieve an order_|_Superuser_|
| *GET* | ```/orders/user/order/{order_id}/``` | _Get user's specific order_|
| *GET* | ```/docs/``` | _View API documentation_|_All users_|

## Python Packages
1. [Flask](https://flask.palletsprojects.com/en/2.2.x/)
2. [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/)
3. [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
4. [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
5. [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
6. [Python-decouple](https://pypi.org/project/python-decouple/)
7. [Pytest](https://docs.pytest.org/en/7.2.x/)

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

### Step 3:
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

