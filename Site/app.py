from flask import Flask, render_template, request, redirect, url_for 
import psycopg2 

app = Flask(__name__) 

@app.route('/') 
def index(): 
	# Connect to the database 
	conn = psycopg2.connect(database="VideoGameSiteDB", user="postgres", 
						password="password", host="172.16.0.14", port="5432")  

	# create a cursor 
	cur = conn.cursor() 

	# Select all products from the table 
	cur.execute('''SELECT * FROM Games''') 

	# Fetch the data 
	data = cur.fetchall() 

	# close the cursor and connection 
	cur.close() 
	conn.close() 

	return render_template('index.html', data=data) 


@app.route('/create', methods=['POST']) 
def create(): 
	conn = psycopg2.connect(database="VideoGameSiteDB", user="postgres", 
						password="password", host="172.16.0.14", port="5432") 

	cur = conn.cursor() 

	# Get the data from the form 
	title = request.form['title'] 
	genre_id = request.form['genre_id']
	release_year = request.form['release_year'] 
	rating = request.form['rating']  

	# Insert the data into the table 
	cur.execute( 
		'''INSERT INTO Games \ 
		(name, price) VALUES (%s, %s, %s, %s)''', 
		(title, genre_id, release_year, rating)) 

	# commit the changes 
	conn.commit() 

	# close the cursor and connection 
	cur.close() 
	conn.close() 

	return redirect(url_for('index')) 


@app.route('/update', methods=['POST']) 
def update(): 
	conn = psycopg2.connect(database="VideoGameSiteDB", user="postgres", 
						password="password", host="172.16.0.14", port="5432") 

	cur = conn.cursor() 

	# Get the data from the form 

	id = request.form['id']
	title = request.form['title'] 
	genre_id = request.form['genre_id']
	release_year = request.form['release_year'] 
	rating = request.form['rating']  

	# Update the data in the table 
	cur.execute( 
		'''UPDATE Games SET title=%s,\ 
		genre_id=%s, release_year=%s, rating=%s WHERE id=%s''', (title, genre_id, release_year, rating, id)) 

	# commit the changes 
	conn.commit() 
	return redirect(url_for('index')) 


@app.route('/delete', methods=['POST']) 
def delete(): 
	conn = psycopg2.connect(database="VideoGameSiteDB", user="postgres", 
						password="password", host="172.16.0.14", port="5432") 
	cur = conn.cursor() 

	# Get the data from the form 
	id = request.form['id'] 

	# Delete the data from the table 
	cur.execute('''DELETE FROM Games WHERE id=%s''', (id,)) 

	# commit the changes 
	conn.commit() 

	# close the cursor and connection 
	cur.close() 
	conn.close() 

	return redirect(url_for('index')) 


if __name__ == '__main__': 
	app.run(debug=True) 
