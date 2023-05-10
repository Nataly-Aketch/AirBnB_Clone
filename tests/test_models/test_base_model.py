#!/usr/bin/python3
"""Unit Testing for Base Model"""
import unittest
import time
from models.base_model import BaseModel

class TestBase(unittest.TestCase):
    """Test the Base Model Class"""
    def test_instantiation(self):
        """Tests instantiation of the BaseModel class"""
        my_model = BaseModel()
        self.assertEqual(str(type(my_model)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(issubclass(type(my_model), BaseModel))
    
    def test_to_dict(self):
        """Tests to_dict() method"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        # self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

    def test_save(self):
        """Tests the save() method"""
        my_model = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        my_model.save()
        diff = my_model.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)




if __name__ == "__main__":
    unittest.main()