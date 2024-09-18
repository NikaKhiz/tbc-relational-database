from faker import Faker
import random
from datetime import datetime

fake = Faker()

def generate_random_author():
    name = fake.first_name()
    surname = fake.last_name()
    from_location = fake.city()
    born_date = fake.date_of_birth(minimum_age=0, maximum_age=100).strftime('%Y-%m-%d')
    
    return (name, surname, from_location, born_date)


def fetch_existing_author_info(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, born_date FROM author;")
    author_info = cursor.fetchall()
    return author_info


def generate_random_book(author_info):
    author_id, born_date_str = random.choice(author_info)

    born_date = datetime.fromisoformat(born_date_str)
    min_release_year = born_date.year + 18
    current_year = datetime.now().year

    if min_release_year > current_year:
        min_release_year = current_year

    release_year = random.randint(min_release_year, current_year)
    release_month = random.randint(1, 12)
    release_day = random.randint(1, 28)

    release_date = datetime(release_year, release_month, release_day).strftime('%Y-%m-%d')
    name = fake.catch_phrase() 
    category = fake.word()
      
    while len(category) < 4:
        category = fake.word()
        
    pages = random.randint(50, 500)

    return (author_id, name, category, pages, release_date)