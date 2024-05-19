from flask import Flask
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection

app = Flask(__name__)

def get_connection(host: str, db_name: str, password: str, user: str) -> connection|None:
    '''Connects to the database'''
    try:
        conn = psycopg2.connect(host=host,
                                dbname=db_name,
                                password=password,
                                user=user,
                                cursor_factory=RealDictCursor)
        return conn
    except psycopg2.Error as e:
        print(f"Error {e} occured!")
        return None

if __name__ == "__main__":

    app.run(debug=True)
