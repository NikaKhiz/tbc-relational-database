from database_generator import DatabaseGenerator 
from database_collector import DatabaseCollector 


def main():
    db = DatabaseGenerator.create()
    db.drop_table('author')
    db.drop_table('books')
    db.create_authors_table()
    db.create_books_table()
    db.populate_authors()
    db.populate_books()
    db.close_connection()


    db_collector = DatabaseCollector.create()
    print("Book with the most pages:", db_collector.books_with_most_pages())
    print("Average number of pages:", db_collector.average_pages_count())
    print("Youngest author:", db_collector.youngest_authors())
    print("Authors without books:", db_collector.authors_without_books())
    print("Authors with more then five books:", db_collector.authors_with_more_than_five_books())
    db_collector.close_connection()
    

    


if __name__ == '__main__':
    main()