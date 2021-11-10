#!/usr/bin/python3
"""
Create a unique FileStorage instance for your application
"""
from .engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
