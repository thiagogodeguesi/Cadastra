import psycopg2
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='config.env')

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def test_connection():
    conn = get_connection()
    conn.close()
    print("✅ Conexão SSL bem-sucedida!")
    