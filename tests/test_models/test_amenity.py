#!/usr/bin/python3
"""Test the Amenity class"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from sqlalchemy import inspect
from sqlalchemy.sql import sqltypes


class test_Amenity(test_basemodel):
    """A unittest to test the Amenity class """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity
        self.inspector = inspect(Amenity)

    def test_name2(self):
        """ test the type of name """
        info = self.inspector.columns['name']
        new = self.value()
        self.assertEqual(type(info.type), sqltypes.String)


if __name__ == "__main__":
    unittest.main()
