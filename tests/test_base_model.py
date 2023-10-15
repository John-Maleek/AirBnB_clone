"""
Test file that test BaseModel
"""
import unittest
import models
from datetime import datetime


BaseModel = models.base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test BaseModel class.
    """

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
        self.assertEqual(obj1.created_at, obj1.updated_at)
        self.assertEqual(obj2.created_at, obj2.updated_at)
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

    # def test_to_dict(self):
        """
        test to_dict method that converts the object attributes to a dictionary
        """
        # ins = BaseModel()
        # ins.id = '135'
        # ins.name = 'siti_alx_stu'
        # ins.num = 99
        # ins.created_at = datetime(2023, 10, 15, 11, 0, 0)
        # ins.updated_at = datetime(2023, 10, 15, 12, 0, 0)

        # expected_dict = {
        #     'id': '135',
        #     'name': 'siti_alx_stu',
        #     '__class__': 'BaseModel',
        #     'created_at': '2023-10-15T11:00:00',
        #     'updated_at': '2023-10-15T12:00:00'
        # }
        # res = ins.to_dict()
        # self.assertEqual(res, expected_dict)

        # expe_attribute = ["id", "created_at",
        #                   "updated_at", "name"
        #                   "num", "name", "__class__"]
        # self.assertEqual(res['__class__'], 'BaseModel')
        # self.assertEqual(res['name'], "siti_alx_stu")
        # self.assertEqual(res['num'], 99)
        # self.assertCountEqual(res.key(), expe_attribute)

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
