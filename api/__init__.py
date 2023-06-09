from flask import Flask
from flask_restx import Api
from .orders.views import order_namespace
from .auth.views import auth_namespace
from .config.config import config_dict
from .utils import db
from .models.orders import Order
from .models.users import User
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

def create_app(config=config_dict['dev']):
    app=Flask(__name__)

    app.config.from_object(config)

    authorizations={
        "Bearer Auth":{
            'type':"apiKey",
            'in':'header',
            'name':"Authorization",
            'description':"Add a JWT with ** Bearer &lt;JWT&gt; to authorize"
        }
    }
    api=Api(app,
        title="Pizza Delivery API",
        description="A REST API for a Pizza Delivery Service",
        authorizations=authorizations,
        security="Bearer Auth"
    )

    api.add_namespace(order_namespace)
    api.add_namespace(auth_namespace, path='/auth')

    db.init_app(app)

    migrate=Migrate(app, db)

    jwt=JWTManager(app)

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'User': User,
            'Order': Order
        }

    return app