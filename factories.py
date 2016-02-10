# -*- encoding: utf-8 -*-
import factory
from factory.alchemy import SQLAlchemyModelFactory
from models import User, db


class UserFactory(SQLAlchemyModelFactory):

    class Meta:
        model = User
        sqlalchemy_session = db.session
        force_flush = True

    email = factory.Sequence(lambda n: u'user%d@example.com' % n)
    first_name = factory.Iterator(['John', 'Jack', 'Joseph', 'Jason', 'Jerry'])
    last_name = factory.Iterator(['Smith', 'Jones', 'Black', 'Brown',
                                  'Anderson'])

