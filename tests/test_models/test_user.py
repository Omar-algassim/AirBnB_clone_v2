#!/usr/bin/python3
"""Test the User class """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from sqlalchemy import inspect
from sqlalchemy.sql import sqltypes


class test_User(test_basemodel):
    """A unittest to test the User class"""

    def __init__(self, *args, **kwargs):
        """Initialize the testcase"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User
        self.inspector = inspect(User)

    def test_first_name(self):
        """ """
        info = self.inspector.columns['first_name']
        new = self.value()
        self.assertEqual(type(info.type), sqltypes.String)

    def test_last_name(self):
        """ """
        info = self.inspector.columns['last_name']
        new = self.value()
        self.assertEqual(type(info.type), sqltypes.String)

    def test_email(self):
        """ """
        info = self.inspector.columns['email']
        new = self.value()
        self.assertEqual(type(info.type), sqltypes.String)

    def test_password(self):
        """ """
        info = self.inspector.columns['password']
        new = self.value()
        self.assertEqual(type(info.type), sqltypes.String)


if __name__ == "__main__":
    unittest.main()
