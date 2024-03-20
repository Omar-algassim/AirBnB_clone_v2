#!/usr/bin/python3
"""Test the review class"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from sqlalchemy import inspect
from sqlalchemy.sql import sqltypes


class test_review(test_basemodel):
    """A unittest to test the Review class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review
        self.inspector = inspect(Review)

    def test_place_id(self):
        """ """
        info = self.inspector.columns['place_id']
        new = self.value()
        self.assertEqual(type(info.type), sqltypes.String)

    def test_user_id(self):
        """ """
        info = self.inspector.columns['user_id']
        new = self.value()
        self.assertEqual(type(info.type), sqltypes.String)

    def test_text(self):
        """ """
        info = self.inspector.columns['text']
        new = self.value()
        self.assertEqual(type(info.type), sqltypes.String)


if __name__ == "__main__":
    unittest.main()
