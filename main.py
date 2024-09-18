from database_generator import BooksGenerator 
from database_collector import DatabaseCollector 


def main():
    db = BooksGenerator.create()
    db.create_authors_table()
    db.create_books_table()
    db.populate_authors()
    db.populate_books()
    db.close_connection()


    db_collector = DatabaseCollector.create()
    print("Book with the most pages:", db_collector.books_with_most_pages())
    print("Average number of pages:", db_collector.average_pages_count())
    db_collector.close_connection()
    


if __name__ == '__main__':
    main()