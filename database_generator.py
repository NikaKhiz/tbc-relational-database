import sqlite3 as sqlite
from utils import * 

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
    
                
    def create_authors_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS author (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                from_location TEXT NOT NULL,
                birth_date TEXT NOT NULL
            );
            """
        
        self.cursor.execute(query)
        self.conn.commit()


    def create_books_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                author_id INTEGER,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                pages INTEGER NOT NULL,
                release_date TEXT NOT NULL,
                FOREIGN KEY (author_id) REFERENCES author(id) ON DELETE CASCADE
            );
            """
        
        self.cursor.execute(query)
        self.conn.commit()


    def is_table_empty(self, table_name):
        query = f"SELECT COUNT(*) FROM {table_name};"
        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]
        return count == 0

    def drop_table(self,table_name):
        query = f'DROP TABLE IF EXISTS {table_name}'
        self.cursor.execute(query)


    def populate_authors(self):
        if self.is_table_empty('author'):

            authors = [generate_random_author() for _ in range(500)]
            query = """
                INSERT INTO author (name, surname, from_location, birth_date)
                VALUES (?, ?, ?, ?);
                """ 

            self.cursor.executemany(query, authors)
            self.conn.commit()

        else:

            print("Author table already contains data.")

        
    
    def populate_books(self):
        if self.is_table_empty('books'):

            author_info = fetch_existing_author_info(self.conn)
            books = [generate_random_book(author_info) for _ in range(1000)]
            query = """
                INSERT INTO books (author_id, name, category, pages, release_date)
                VALUES (?, ?, ?, ?, ?);
                """ 

            self.cursor.executemany(query, books)
            self.conn.commit()

        else:
            print("Books table already contains data.")



    def close_connection(self):
        self.conn.close()
