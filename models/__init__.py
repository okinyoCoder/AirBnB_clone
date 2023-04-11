"""a unique FileStorage instance for your application"""
from models.engine.file_storage.py import Filestorage
storage = FileStorage()
storage.reload()
