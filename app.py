from flask import Flask, jsonify, render_template, request, redirect
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
        cur.execute("SELECT todo_id as id, item FROM todolist;")
        all_items = cur.fetchall()
    conn.close()
    return render_template('index.html', items=all_items), 200


@app.route('/add_item', methods=['POST'])
def add_item():
    new_item = request.form['item']
    conn = get_connection(os.environ["DB_HOST"], os.environ["DB_NAME"],
                          os.environ["DB_PASS"], os.environ["DB_USER"])
    with conn.cursor() as cur:
        cur.execute("INSERT INTO todolist (item) VALUES (%s)", (new_item,))
    conn.commit()
    conn.close()
    return redirect('/')


# @app.route('/delete_item', methods=['POST'])
# def delete_item():
#     new_item = request.form['item']
#     conn = get_connection(os.environ["DB_HOST"], os.environ["DB_NAME"],
#                           os.environ["DB_PASS"], os.environ["DB_USER"])
#     with conn.cursor() as cur:
#         cur.execute("INSERT INTO todolist (item) VALUES (%s)", (new_item,))
#     conn.commit()
#     conn.close()
#     return redirect('/')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True)
