from flask import Flask, render_template, request, redirect, url_for, jsonify
import psycopg2 
import os

app = Flask(__name__) 
# db_url = "postgresql://five_two_db_user:kkUsE52r2PnExnZrJvL3oUue9Tzq2jxT@dpg-cog0av8l5elc73dm3iq0-a.oregon-postgres.render.com/five_two_db"
db_url = os.environ.get("DATABASE_URL")


conn = psycopg2.connect(db_url)

cur = conn.cursor() 
cur.execute( 
	'''CREATE TABLE IF NOT EXISTS products (id serial PRIMARY KEY, name varchar(100), price float);''') 
# cur.execute( 
# 	'''INSERT INTO products (name, price) VALUES ('Apple', 1.99), ('Orange', 0.99), ('Banana', 0.59);''') 

conn.commit() 

cur.close() 
conn.close() 


@app.route('/') 
def index(): 
	conn = psycopg2.connect(db_url)
	cur = conn.cursor() 

	cur.execute('''SELECT * FROM products''') 

	data = cur.fetchall() 
	cur.close() 
	conn.close() 

	return render_template('index.html', data=data) 


@app.route('/api/products', methods=['GET'])
def get_products():
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()

    cur.execute('''SELECT * FROM products''')

    data = cur.fetchall()
    cur.close()
    conn.close()

    # Convert the fetched data directly to JSON
    return jsonify(data)


@app.route('/create', methods=['POST']) 
def create(): 
	conn = psycopg2.connect(db_url) 

	cur = conn.cursor() 

	name = request.form['name'] 
	price = request.form['price'] 
	cur.execute( '''INSERT INTO products (name, price) VALUES (%s, %s)''', (name, price)) 
	conn.commit() 
	cur.close() 
	conn.close() 
	return redirect(url_for('index')) 


@app.route('/update', methods=['POST']) 
def update(): 
	conn = psycopg2.connect(db_url) 
	cur = conn.cursor() 
	name = request.form['name'] 
	price = request.form['price'] 
	id = request.form['id'] 

	cur.execute( '''UPDATE products SET name=%s, price=%s WHERE id=%s''', (name, price, id)) 

	conn.commit() 
	return redirect(url_for('index')) 


@app.route('/delete', methods=['POST']) 
def delete(): 
	conn = psycopg2.connect(db_url)
	id = request.form['id'] 
	cur = conn.cursor()
	cur.execute('''DELETE FROM products WHERE id=%s''', (id,)) 
	conn.commit() 
	cur.close() 
	conn.close() 

	return redirect(url_for('index')) 


if __name__ == '__main__': 
	app.run(debug=True) 
