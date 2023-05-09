#!/usr/bin/python3
"""this module defines the BaseModel class"""
from datetime import datetime
from datetime import timedelta
import uuid


class BaseModel():
    """defines all common attributes/methods for other classes"""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        """prints informal string representation of the class"""
        dict1 = {'id': self.id, 'created_at': self.created_at,
                 'updated_at': self.updated_at}
        dict1.update(**self.__dict__)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, dict1)

    def save(self):
        """updates the instance attribute with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns dict representation of the instance"""
        dict1 = {'id': self.id, 'created_at': self.created_at.isoformat(),
                 'updated_at': self.updated_at.isoformat(), '__class__':
                 type(self).__name__}
        dict1.update(**self.__dict__)
        return dict1

    def __init__(self, *args, **kwargs):
        """Initializes class BaseModel"""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    v = getattr(self, k)
                else:
                    v = setattr(self, k, v)
