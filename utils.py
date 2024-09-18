from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

def generate_random_author():
    today = datetime.now()
    min_birth_date = today - timedelta(days=365 * 18)

    name = fake.first_name()
    surname = fake.last_name()
    from_location = fake.city()
    
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=100).strftime('%Y-%m-%d')
    
    # ensure that birth date is no later than the min_birth_date
    while datetime.fromisoformat(birth_date) > min_birth_date:
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=100).strftime('%Y-%m-%d')
    
    return (name, surname, from_location, birth_date)


def fetch_existing_author_info(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, birth_date FROM author;")
    author_info = cursor.fetchall()
    return author_info

def generate_random_book(author_info):
    author_id, birth_date_str = random.choice(author_info)

    birth_date = datetime.fromisoformat(birth_date_str)
    min_release_year = birth_date.year + 18
    current_year = datetime.now().year

    if min_release_year > current_year:
        min_release_year = current_year

    release_year = random.randint(min_release_year, current_year)
    release_month = random.randint(1, 12)
    release_day = random.randint(1, 28)

    release_date = datetime(release_year, release_month, release_day).strftime('%Y-%m-%d')
    name = fake.catch_phrase() 
    category = fake.word()
      
    # ensure that category length is long enough
    while len(category) < 4:
        category = fake.word()
        
    pages = random.randint(50, 500)

    return (author_id, name, category, pages, release_date)
