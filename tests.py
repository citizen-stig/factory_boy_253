# -*- encoding: utf-8 -*-
import unittest

from models import db, User
from factories import UserFactory
from application import app


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://flask:flask@localhost:5432/test_factory_boy'
        cls.app.config['SQLALCHEMY_ECHO'] = True
        db.app = cls.app

        db.init_app(cls.app)
        cls._ctx = cls.app.test_request_context()
        cls._ctx.push()
        db.drop_all()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.engine.dispose()
        db.drop_all()

    def setUp(self):
        self.client = self.app.test_client()
        self._ctx = self.app.test_request_context()
        self._ctx.push()
        db.session.begin(subtransactions=True)

    def tearDown(self):
        db.session.close()
        db.session.rollback()
        self._ctx.pop()


class ProblemsTestCase(BaseTestCase):

    def test_str_conversion(self):
        # Replace user creation with this to make test work
        # user = User(first_name='John', last_name='Doe', email='test@example.com')
        # db.session.add(user)
        # db.session.commit()
        user = UserFactory()
        some_id = u'4242'
        user.some_id = some_id
        db.session.commit()
        again_user = User.query.get(user.id)
        self.assertEqual(again_user.some_id, int(some_id))