from flask import Flask, render_template, url_for, request
from flaskext.mysql import MySQL
import csv

app = Flask(__name__)
mysql = MySQL()

# Note to self: This will need to be changed eventually
app.config['MYSQL_DATABASE_USER'] = 'rpwilliams96'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'rpwilliams96'
app.config['MYSQL_DATABASE_HOST'] = 'mysql.cs.ksu.edu'
mysql.init_app(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
	return render_template('add.html')

# @app.route('/ideas', methods=['GET', 'POST'])
# def ideas():
# 	return render_template('ideas.html')

def connect_to_mySQL():
	""" Connects to mySQL """
	return mysql.connect()

def execute_query(query, args=()):
	""" Executes a query.
		@param {query} The query to be executed
		@param {args} The arguments.
		@return The rows in the query.
	"""
	conn = connect_to_mySQL()
	cursor = conn.cursor()
	cursor.execute(query, args)
	rows = cursor.fetchall()
	conn.commit()
	cursor.close()
	return rows

@app.route('/ideas', methods=['GET', 'POST'])
def ideas():
	""" Adds an idea to the database """
	idea = {
		'title': request.form['title'],
		'category': request.form['category'],
		'description': request.form['description']
	}
	query = execute_query("""INSERT INTO Ideas(name, description, category) VALUES (%s, %s, %s)""", [idea['title'], idea['category'], idea['description']])
	return render_template('ideas.html')

@app.route("/viewdb")
def viewdb():
	rows = execute_query("""SELECT * FROM Ideas;""")
	return '<br>'.join(str(row) for row in rows) # Displays everything in db in the browser

if __name__ == '__main__':
  app.run(debug = True)