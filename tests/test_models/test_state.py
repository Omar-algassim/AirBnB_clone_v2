#!/usr/bin/python3
"""Test the State class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from sqlalchemy import inspect
from sqlalchemy.sql import sqltypes


class test_state(test_basemodel):
    """A unittest for the State class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State
        self.inspector = inspect(State)

    def test_name3(self):
        """ """
        info = self.inspector.columns['name']
        new = self.value()
        self.assertEqual(type(info.type), sqltypes.String)


if __name__ == "__main__":
    unittest.main()
