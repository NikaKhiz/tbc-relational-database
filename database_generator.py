import sqlite3 as sqlite

class BooksGenerator():
    def __init__(self, conn, cursor) -> None:
        self.conn = conn
        self.cursor = cursor

    @property
    def conn(self):
        return self._conn

    @conn.setter
    def conn(self, conn):
        self._conn = conn

    @property
    def cursor(self):
        return self._cursor
    
    @cursor.setter
    def cursor(self, cursor):
        self._cursor = cursor

    @classmethod
    def create(cls):
        conn = sqlite.connect('books.db')
        cursor = conn.cursor()

        return cls(conn, cursor)
    