#!/usr/bin/python3
"""
Defines the base model
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes an instance
        """
        if kwargs is not None:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """
        String representation when instance is printed
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Save updates to an instance
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of an instance
        """
        self.__dict__.update({"__class__": type(self).__name__,
                              "updated_at": self.updated_at.isoformat(),
                              "id": self.id,
                              "created_at": self.created_at.isoformat()})
        return self.__dict__
