#!/usr/bin/python3
"""Unit Testing for Base Model"""
from contextlib import redirect_stdout
from datetime import datetime
from io import StringIO
import io
from models.user import User
import unittest
import time


class TestInstantation(unittest.TestCase):
    """Test the User Class"""
    def test_instantiation(self):
        user = User()
        self.assertIsInstance(user, User)

    def test_id_type(self):
        user = User()
        self.assertEqual(type(user.id), str)

    def test_uuid(self):
        user = User()
        other_user = User()
        self.assertNotEqual(user.id, other_user.id)

    def test_datetime(self):
        user = User()
        self.assertNotEqual(user.created_at, datetime.now())

    def test_datetime_type(self):
        user = User()
        self.assertEqual(type(user.created_at), datetime)

    def test_kwargs(self):
        user = User(new_name="first")
        self.assertTrue(hasattr(user, 'new_name'))


class TestMethods(unittest.TestCase):
    """Tests public instance methods of basemodel"""
    def test_to_dict_type(self):
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(type(user_dict), dict)

    def test_dict_datetime_type(self):
        user = User()
        new_dict = user.to_dict()
        self.assertEqual(type(new_dict.get('created_at')), str)

    def test_save(self):
        """Tests the save() method"""
        user = User()
        time.sleep(0.5)
        date_now = datetime.now()
        user.save()
        diff = user.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_str(self):
        user = User()
        expected = "[{}] ({}) {}\n".format(type(user).__name__, user.id,
                                           user.__dict__)
        with io.StringIO() as buf, redirect_stdout(buf):
            print(user)
            self.assertEqual(buf.getvalue(), expected)


if __name__ == "__main__":
    unittest.main()
