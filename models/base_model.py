#!/usr/bin/python3
"""this module defines the BaseModel class"""
from datetime import datetime
from datetime import timedelta
import uuid


class BaseModel():
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initializes class BaseModel"""
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)
        if len(kwargs) != 0:
            d = '%Y-%m-%dT%H:%M:%S.%f'
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    self.__dict__[k] = datetime.strptime(v, d)
                else:
                    self.__dict__[k] = v

    def __str__(self):
        """prints informal string representation of the class"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates the instance attribute with current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns dict representation of the instance"""
        dict1 = self.__dict__.copy()
        dict2 = {'id': self.id, 'created_at': self.created_at.isoformat(),
                 'updated_at': self.updated_at.isoformat(), '__class__':
                 type(self).__name__}
        dict1.update(dict2)
        return dict1
