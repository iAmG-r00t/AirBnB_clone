#!/usr/bin/python3
"""
Test suite for file_storage engine
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def test_all(self):
        base = BaseModel()
        storage = FileStorage()
        self.assertEqual(base.__class__, BaseModel)
        self.assertEqual(storage.reload(), None)
        # base.save()
