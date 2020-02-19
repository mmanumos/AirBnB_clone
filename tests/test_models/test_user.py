#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
import unittest
import pep8
import models
from models.base_model import BaseModel
""" import moduls """
class verify_pep8(unittest.TestCase):
    """ class - PEP 8 validated """
    def test_pep8(self):
        """ method - PEP 8 test """
        check = pep8.Checker("models/user.py", show_source=True)
        file_error= check.check_all()

class verify_work(unittest.TestCase):
    """ funcionality test """

    def setUp(self):
        """ Method called immediately before calling the test method """
        pass

    def tearDown(self):
        """ Method called immediately after calling the test method """
        try:
            remove("file.json")
        except:
            pass
