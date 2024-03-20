#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class test_create_command(unittest.TestCase):
    """Unittests for testing create from the HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        if (type(storage) is FileStorage):
                FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     'BaseModel not support database model')
    def test_create_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as foutput:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(correct, foutput.getvalue().strip())

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     'BaseModel not support database model')
    def test_create_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as foutput:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(correct, foutput.getvalue().strip())

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     'BaseModel not support database model')
    def test_create_invalid_syntax(self):
        correct = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as foutput:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(correct, foutput.getvalue().strip())
        correct = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as foutput:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(correct, foutput.getvalue().strip())

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     'BaseModel not support database model')
    def test_create_object(self):
        with patch("sys.stdout", new=StringIO()) as foutput:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(foutput.getvalue().strip()))
            testKey = "BaseModel.{}".format(foutput.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as foutput:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(foutput.getvalue().strip()))
            testKey = "User.{}".format(foutput.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as foutput:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(foutput.getvalue().strip()))
            testKey = "State.{}".format(foutput.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as foutput:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(foutput.getvalue().strip()))
            testKey = "City.{}".format(foutput.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as foutput:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(foutput.getvalue().strip()))
            testKey = "Amenity.{}".format(foutput.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as foutput:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(foutput.getvalue().strip()))
            testKey = "Place.{}".format(foutput.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as foutput:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(foutput.getvalue().strip()))
            testKey = "Review.{}".format(foutput.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
