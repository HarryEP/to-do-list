'''Flask application to run a to do list'''
import os
from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection
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
    except psycopg2.Error as err:
        print(f"Error {err} occurred!")
        return None


@app.route('/')
def index():
    '''sorts by and views all items in the database'''
    sort_by = request.args.get('sort_by', 'item')
    if sort_by not in ['item', 'date', 'completed', 'priority']:
        sort_by = 'item'
    conn = get_connection(os.environ["DB_HOST"], os.environ["DB_NAME"],
                          os.environ["DB_PASS"], os.environ["DB_USER"])
    if conn is None:
        return 'Failure to connect to server', 500
    with conn.cursor() as cur:
        cur.execute(
            f"""SELECT todo_id as id, item, created_at as date, completed, completed_at, priority
              FROM todo ORDER BY {sort_by};""")
        all_items = cur.fetchall()
    conn.close()
    return render_template('index.html', items=all_items), 200


@app.route('/add_item', methods=['POST'])
def add_item():
    '''adds an item to the database'''
    new_item = request.form['item']
    priority = int(request.form['priority'])
    conn = get_connection(os.environ["DB_HOST"], os.environ["DB_NAME"],
                          os.environ["DB_PASS"], os.environ["DB_USER"])
    if conn is None:
        return 'Failure to connect to server', 500
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO todo (item, priority) VALUES (%s, %s)", (new_item, priority))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/complete_item/<int:item_id>', methods=['POST'])
def complete_item(item_id):
    '''marks the item as completed'''
    conn = get_connection(os.environ["DB_HOST"], os.environ["DB_NAME"],
                          os.environ["DB_PASS"], os.environ["DB_USER"])
    if conn is None:
        return 'Failure to connect to server', 500
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE todo SET completed = TRUE, completed_at = NOW() where todo_id = %s", (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/delete_item/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    '''removes selected item from the database'''
    conn = get_connection(os.environ["DB_HOST"], os.environ["DB_NAME"],
                          os.environ["DB_PASS"], os.environ["DB_USER"])
    if conn is None:
        return 'Failure to connect to server', 500
    with conn.cursor() as cur:
        cur.execute("DELETE FROM todo WHERE todo_id = %s", (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/update_item/<int:item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    '''function to update a selected item in the database to request change'''
    conn = get_connection(os.environ["DB_HOST"], os.environ["DB_NAME"],
                          os.environ["DB_PASS"], os.environ["DB_USER"])
    if conn is None:
        return 'Failure to connect to server', 500
    if request.method == "GET":
        with conn.cursor() as cur:
            cur.execute(
                "SELECT todo_id as id, item FROM todo WHERE todo_id = %s;", (item_id,))
            item = cur.fetchone()
        conn.close()
        return render_template('patch_item.html', item=item)
    if request.method == "POST":
        updated_item = request.form['item']
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE todo SET item = %s WHERE todo_id = %s", (updated_item, item_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(error):
    '''if 404 error, show this page'''
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True)
