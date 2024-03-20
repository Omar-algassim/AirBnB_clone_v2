#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import pycodestyle
from models.base_model import BaseModel
from models import storage
import MySQLdb
import os


class test_DBStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def test_pycode_style(self):
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, 'PEP8 should be fixed')

    def test_DBStorage_docs(self):
        from models.engine.db_storage import DBStorage
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)


if __name__ == "__main__":
    unittest.main()
