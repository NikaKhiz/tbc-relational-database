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
    
                
    def create_authors_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS author (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                from_location TEXT NOT NULL,
                born_date TEXT NOT NULL
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


    def close_connection(self):
        self.conn.close()