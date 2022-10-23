import os
import psycopg2
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

print(os.environ['DB_HOST'])
conn = psycopg2.connect(
    host=os.environ['DB_HOST'],
    database="flask_db",
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('CREATE TABLE IF NOT EXISTS books (id serial PRIMARY KEY,'
            'title varchar (150) NOT NULL,'
            'author varchar (50) NOT NULL,'
            'pages_num integer NOT NULL,'
            'review text,'
            'date_added date DEFAULT CURRENT_TIMESTAMP);'
            )

# Insert data into the table

cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens',
             489,
             'A great classic!')
            )


cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic!')
            )

conn.commit()

cur.close()
conn.close()
