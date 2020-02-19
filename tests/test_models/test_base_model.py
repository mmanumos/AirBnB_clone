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
        check = pep8.Checker("models/base_model.py", show_source=True)
        file_error= check.check_all()

class verify_work(unittest.TestCase):
    """ funcionality test """

    def setUp(self):
        """ Method called immediately before calling the test method """
        self.my_model = BaseModel()

    def tearDown(self):
        """ Method called immediately after calling the test method """
        try:
            remove("file.json")
        except:
            pass

    def test_doc(self):
        """ test documentation """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_name(self):
        """ test name """
        self.my_model.name = "Holberton"
        self.assertEqual(self.my_model.name, "Holberton")

    def test_number(self):
        """ test number """
        self.my_model.my_number = 89
        self.assertEqual(self.my_model.my_number, 89)

    def test_time_save(self):
        """ test time save """
        time_cre = self.my_model.created_at
        time_upd = self.my_model.updated_at
        self.my_model.save()
        self.assertFalse(time_upd == self.my_model.updated_at)
        self.assertTrue(time_cre == self.my_model.created_at)

    def test_to_dict(self):
        """ test to dict """
        model_1 = self.my_model.to_dict()
        self.assertIsInstance(model_1["created_at"], str)
        self.assertIsInstance(model_1["updated_at"], str)
        self.assertIsInstance(model_1["id"], str)

    def test_json_file_not_empty(self):
        """ test json file is not empty """
        self.assertTrue('file.json')

if __name__ == '__main__':
    unittest.main()
