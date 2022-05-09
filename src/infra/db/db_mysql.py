import mysql.connector
from mysql.connector import Error
from decouple import config


class DBConnection:

    _connect = None
    __access = {
    "host": config("HOST"),
    "username": config("USERNAME"),
    "password": config("PASSWORD"),
    "db": config("DB")
}

    def __init__(self) -> None:
        self._connect = mysql.connector.connect(**self.__access)
         
         
    def write_query(self, query: str):
        try:
            cursor = self._connect.cursor()
            cursor.execute(query)
            id = cursor.lastrowid
            self._connect.commit()
        except Error as err:
            return err
        else:
            return id

    
    def read_query(self, query: str):
        try:
            result = None
            cursor = self._connect.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as err:
            return err
        else:
            return result