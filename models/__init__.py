#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
from models.engine.file_storage import FileStorage
""" import moduls """

storage = FileStorage()
storage.reload()
