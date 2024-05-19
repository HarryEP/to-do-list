from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection
import os
from dotenv import load_dotenv

app = Flask(__name__)


def get_connection(host: str, db_name: str, password: str, user: str) -> connection | None:
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


@app.route('/')
def index():
    conn = get_connection(os.environ["DB_HOST"], os.environ["DB_NAME"],
                          os.environ["DB_PASS"], os.environ["DB_USER"])
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM todolist;")
        todolist = cur.fetchall()
    conn.close()
    return jsonify(todolist)


if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True)
