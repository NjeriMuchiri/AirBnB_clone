#!/usr/bin/python3
"""This is the base model class for AirBnB"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """This is the base class that defines all common attributes
    and methods of all other classes that will inherit from it"""
    def __init__(self, *args, **kwargs):
        """This is the base model instance
        Args:
            args: This won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique random id
            created_at: creation date
            updated_at: updated date"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string
        Return:
            returns a string of class name, the id and dictionary
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def __repr__(self):
        """returns a string representation"""
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_to to current"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary of the class
        Return:
            returns a dictionary of all the key values in __dict__"""
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def delete(self):
        """deletes object"""
        models.storage.delete(self)
