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
    def __init__(self):
        """
        Initializes an instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
