import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="deepseek",
        user="postgres",  # Replace with your PostgreSQL username
        password="Fliph106",  # Replace with your PostgreSQL password
        host="localhost",
        port="5433"
    )
    return conn