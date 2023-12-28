from flask import Flask, render_template, request, redirect, url_for 
import psycopg2 

app = Flask(__name__) 

@app.route('/') 
def index(): 
	# Connect to the database 
	conn = psycopg2.connect(database="ElectronicLibraryDb", user="postgres", 
						password="password", host="172.16.0.13", port="5432")  

	# create a cursor 
	cur = conn.cursor() 

	# Select all products from the table 
	cur.execute('''SELECT * FROM books''') 

	# Fetch the data 
	data = cur.fetchall() 

	# close the cursor and connection 
	cur.close() 
	conn.close() 

	return render_template('index.html', data=data) 


@app.route('/create', methods=['POST']) 
def create(): 
	conn = psycopg2.connect(database="ElectronicLibraryDb", user="postgres", 
						password="password", host="172.16.0.13", port="5432") 

	cur = conn.cursor() 

	# Get the data from the form 
	title = request.form['title'] 
	author = request.form['author']
	genre = request.form['genre'] 
	publication_year = request.form['publication_year']  

	# Insert the data into the table 
	cur.execute( 
		'''INSERT INTO books (title, author, genre, publication_year) VALUES (%s, %s, %s, %s)''', 
		(title, author, genre, publication_year)) 

	# commit the changes 
	conn.commit() 

	# close the cursor and connection 
	cur.close() 
	conn.close() 

	return redirect(url_for('index')) 


@app.route('/update', methods=['POST']) 
def update(): 
	conn = psycopg2.connect(database="ElectronicLibraryDb", user="postgres", 
						password="password", host="172.16.0.13", port="5432") 

	cur = conn.cursor() 

	# Get the data from the form 

	book_id = request.form['book_id']
	title = request.form['title'] 
	author = request.form['author']
	genre = request.form['genre'] 
	publication_year = request.form['publication_year']  

	# Update the data in the table 
	cur.execute( 
		'''UPDATE books SET title=%s, author=%s, genre=%s, publication_year=%s WHERE id=%s''', (title, author, genre, publication_year)) 

	# commit the changes 
	conn.commit() 
	return redirect(url_for('index')) 


@app.route('/delete', methods=['POST']) 
def delete(): 
	conn = psycopg2.connect(database="ElectronicLibraryDb", user="postgres", 
						password="password", host="172.16.0.13", port="5432") 
	cur = conn.cursor() 

	# Get the data from the form 
	book_id = request.form['book_id'] 

	# Delete the data from the table 
	cur.execute('''DELETE FROM books WHERE id=%s''', (book_id)) 

	# commit the changes 
	conn.commit() 

	# close the cursor and connection 
	cur.close() 
	conn.close() 

	return redirect(url_for('index')) 


if __name__ == '__main__': 
	app.run(debug=True) 
