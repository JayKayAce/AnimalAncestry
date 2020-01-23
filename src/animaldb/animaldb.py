"""
Database functions for handling Animals and their relations
Created: 2020-01-23
Author: Jesper Kjær Sørensen
"""

import sqlite3
import pathlib

class DB:
    __db = None
    path = None
    
    def __init__(self, path = None):
        
        if path:
            self.path = pathlib.Path(path)
            self.__db = sqlite3.connect(self.path)
        else:
            self.path = pathlib.Path("./test.db")



if __name__ == "__main__":
    pass
    