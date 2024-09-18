from database_generator import BooksGenerator 


def main():
    db = BooksGenerator.create()
    db.create_authors_table()
    db.create_books_table()
    db.close_connection()

    


if __name__ == '__main__':
    main()