#!/usr/bin/python3

"""
Test file that test BaseModel
"""
import unittest
import models
import inspect
import pep8 as pycodestyle
from datetime import datetime
from models.base_model import BaseModel
BaseModel = models.base_model.BaseModel
module_docs = models.base_model.__doc__


class TestBaseModel(unittest.TestCase):
    """
    Test BaseModel class.
    """
    @classmethod
    def setUpClass(self):
        """
        set up method for all test function.
        """
        self.base_mth = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_datetime(self):
        """
        test current datetime update function.
        """
        t1 = datetime.now()
        obj1 = BaseModel()
        t2 = datetime.now()
        self.assertTrue(t1 <= obj1.created_at <= t2)

        t1 = datetime.now()
        obj2 = BaseModel()
        t2 = datetime.now()
        self.assertTrue(t1 <= obj2.created_at <= t2)
        self.assertNotEqual(obj1.created_at, obj1.updated_at)
        self.assertNotEqual(obj2.created_at, obj2.updated_at)
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)

    def test_save_method_updated_at(self):
        """
        test the save method that updates the updated_at attribute.
        """
        obj = BaseModel()
        orgnl_updated_at = obj.updated_at
        obj.save()

        self.assertNotEqual(obj.updated_at, orgnl_updated_at)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict(self):
        """
        test to_dict method that converts the object attributes to a dictionary
        """
        ins = BaseModel()
        ins.id = '135'
        ins.name = 'siti_alx_stu'
        ins.num = 99
        ins.created_at = datetime(2023, 10, 15, 11, 0, 0)
        ins.updated_at = datetime(2023, 10, 15, 12, 0, 0)
        res = ins.to_dict()

        expe_attribute = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "num",
                          "__class__"
                          ]
        self.assertEqual(res['__class__'], 'BaseModel')
        self.assertEqual(res['name'], "siti_alx_stu")
        self.assertEqual(res['num'], 99)
        self.assertCountEqual(res.keys(), expe_attribute)

    def test_str(self):
        """
        test displayed value from __str__ method.
        """
        ins = BaseModel()
        ins.id = '124'
        ins.name = 'alx'

        expe_str = "[BaseModel] ({}) {}".format(ins.id, ins.__dict__)
        res = str(ins)
        self.assertEqual(res, expe_str)

    def test_uuid(self):
        """
        Test uuid that generate unique id.
        """
        ins1 = BaseModel()
        ins2 = BaseModel()
        for ins in [ins1, ins2]:
            uuid = ins.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)

        self.assertNotEqual(ins1.id, ins2.id)

    def test_pep8_passeing(self):
        """
        test models/base_model.py file pass pep8 documentation
        """
        for pth in ['models/base_model.py',
                    'tests/test_models/test_base_model.py']:
            with self.subTest(pth=pth):
                err = pycodestyle.Checker(pth).check_all()
                self.assertEqual(err, 0)

    def test_module_docs(self):
        """
        test for module docstring exist.
        """
        self.assertIsNot(module_docs, None)
        self.assertTrue(len(module_docs) > 1)

    def test_class_doc(self):
        """
        test docstring for BaseModel class.
        """
        self.assertIsNot(BaseModel.__doc__, None)
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_method_docs(self):
        """
        Test for method docstring.
        """
        for mth in self.base_mth:
            self.assertIsNot(
                    mth[1].__doc__, None,
                    "{:s} method need docstring".format(mth[0]))
            self.assertTrue(
                    len(mth[1].__doc__) > 1,
                    "{:} method need docs".format(mth[0]))
