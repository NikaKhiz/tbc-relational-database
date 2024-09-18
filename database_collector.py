import sqlite3 as sqlite
from utils import * 
import json

class DatabaseCollector():
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
    

    def books_with_most_pages(self):

        max_pages_query = """
            SELECT MAX(pages) FROM books;
            """
        self.cursor.execute(max_pages_query)

        max_pages = self.cursor.fetchone()[0]
        
        query = """
            SELECT name, pages
            FROM books
            WHERE pages = ?;
            """
        
        self.cursor.execute(query, (max_pages,))

        return json.dumps(self.cursor.fetchall(), indent=4)


    def close_connection(self):
        self.conn.close()