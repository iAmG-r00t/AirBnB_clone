#!/usr/bin/python3
"""
Defines the base model
"""
import uuid
import datetime

class BaseModel:
    """
    Defines all common attributes and methods for other classes
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        
