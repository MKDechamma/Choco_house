from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def create_connection():
    conn = sqlite3.connect('chocolate_house.db')
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        flavor_name TEXT NOT NULL,
                        description TEXT,
                        season TEXT
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients_inventory (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ingredient_name TEXT NOT NULL,
                        quantity INTEGER NOT NULL,
                        unit TEXT
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_feedback (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_name TEXT,
                        flavor_suggestion TEXT,
                        allergy_concern TEXT
                    )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_flavor', methods=['GET', 'POST'])
def add_flavor():
    if request.method == 'POST':
        flavor_name = request.form['flavor_name']
        description = request.form['description']
        season = request.form['season']
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO seasonal_flavors (flavor_name, description, season)
                          VALUES (?, ?, ?)''', (flavor_name, description, season))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_flavor.html')

@app.route('/add_ingredient', methods=['GET', 'POST'])
def add_ingredient():
    if request.method == 'POST':
        ingredient_name = request.form['ingredient_name']
        quantity = request.form['quantity']
        unit = request.form['unit']
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO ingredients_inventory (ingredient_name, quantity, unit)
                          VALUES (?, ?, ?)''', (ingredient_name, quantity, unit))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_ingredient.html')

@app.route('/add_feedback', methods=['GET', 'POST'])
def add_feedback():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        flavor_suggestion = request.form['flavor_suggestion']
        allergy_concern = request.form['allergy_concern']
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO customer_feedback (customer_name, flavor_suggestion, allergy_concern)
                          VALUES (?, ?, ?)''', (customer_name, flavor_suggestion, allergy_concern))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_feedback.html')

@app.route('/view_flavors')
def view_flavors():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seasonal_flavors")
    flavors = cursor.fetchall()
    conn.close()
    return render_template('view_flavors.html', flavors=flavors)

@app.route('/view_inventory')
def view_inventory():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ingredients_inventory")
    ingredients = cursor.fetchall()
    conn.close()
    return render_template('view_inventory.html', ingredients=ingredients)

@app.route('/view_feedback')
def view_feedback():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer_feedback")
    feedbacks = cursor.fetchall()
    conn.close()
    return render_template('view_feedback.html', feedbacks=feedbacks)

if __name__ == '__main__':
    create_tables()
    app.run(host='0.0.0.0', port=5000)

