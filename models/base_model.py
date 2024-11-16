#!/usr/bin/env python3
"""Base model class"""
import uuid
from datetime import datetime


class BaseModel:
    """Base model class
        that defines all common attributes/methods
        for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel."""
        from models import storage

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in {"created_at", "updated_at"}:
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Function that update updated_at attribute"""
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Function that returns a dictionary
            containing all keys/values """
        result = self.__dict__.copy()
        result['__class__'] = type(self).__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return (result)
