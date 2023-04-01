import unittest
from .. import create_app
from ..config.config import config_dict
from ..utils import db
from ..models.users import User
from werkzeug.security import generate_password_hash



class UserTestCase(unittest.TestCase):

    def setup(self):
        self.app = create_app(config=config_dict['testing'])

        self.appctx = self.app.app_context()

        self.appctx.push()

        self.client = self.app.test_client()

        db.create_all()

    def tearDown(self):
        db.drop_all()

        self.appctx.pop()

        self.app = None
        
        self.client = None

    def test_user_registration(self):
        data = {
            "username": "testuser",
            "email":  "testuser@company.com",
            "password": "password"
        }

        response = self.client.post('/auth/signup', json=data)

        user = User.query.filter_by(email="testuser@company.com").first()

        assert user.username == "testuser"

        assert response.status_code == 201 