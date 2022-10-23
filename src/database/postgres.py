
import os
from dotenv import load_dotenv, find_dotenv
import psycopg2
load_dotenv(find_dotenv())


class Database():
    @staticmethod
    def get_db_connection():
        conn = psycopg2.connect(host=os.environ['DB_HOST'],
                                database='flask_db',
                                user=os.environ['DB_USER'],
                                password=os.environ['DB_PASSWORD'])
        return conn
