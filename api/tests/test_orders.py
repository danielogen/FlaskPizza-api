import unittest
from .. import create_app
from ..config.config import config_dict
from ..models.orders import Order
from ..utils import db

class OrderTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config=config_dict['test'])
        self.appctx = self.app.app_context()
        
        self.appctx.push()

        self.client = self.app.test_client()

        db.create_all()
    
    def tearDown(self):
        db.drop_all()

        self.app=None

        self.appctx.pop()

        self.client=None