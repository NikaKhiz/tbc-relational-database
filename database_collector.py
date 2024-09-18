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


    def average_pages_count(self):
        query = """
            SELECT AVG(pages) FROM books;
            """
        self.cursor.execute(query)
        return round(self.cursor.fetchone()[0], 2)


    def youngest_authors(self):
        youngest_date_query = """
            SELECT MAX(birth_date) FROM author;
        """
        self.cursor.execute(youngest_date_query)
        youngest_date = self.cursor.fetchone()[0]

        query = """
            SELECT name, surname, birth_date
            FROM author
            WHERE birth_date = ?;
        """
        self.cursor.execute(query, (youngest_date,))

        return json.dumps(self.cursor.fetchall(), indent=4)  


    def authors_without_books(self):
        query = """
            SELECT id, name, surname
            FROM author
            WHERE id NOT IN (SELECT author_id FROM books);
        """
        self.cursor.execute(query)
        return json.dumps(self.cursor.fetchall(), indent=4)  
    

    def authors_with_more_then_three_book(self):
       query = """
           SELECT a.name, a.surname, COUNT(b.id) as book_count
           FROM author a
           INNER JOIN books b ON a.id = b.author_id
           GROUP BY a.name, a.surname
           HAVING COUNT(b.id) > 3
           LIMIT 5;
       """
       self.cursor.execute(query)
       return json.dumps(self.cursor.fetchall(), indent=4)  


    def close_connection(self):
        self.conn.close()