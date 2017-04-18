from flask import Flask, render_template, url_for, request
from flaskext.mysql import MySQL
import csv

app = Flask(__name__)
mysql = MySQL()

# Note to self: This will need to be changed eventually
app.config['MYSQL_DATABASE_USER'] = 'rpwilliams96'
app.config['MYSQL_DATABASE_PASSWORD'] = 't0rpedo02'
app.config['MYSQL_DATABASE_DB'] = 'rpwilliams96'
app.config['MYSQL_DATABASE_HOST'] = 'mysql.cs.ksu.edu'
mysql.init_app(app)

""" App route functions """

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
	return render_template('add.html')

@app.route('/ideas', methods=['GET'])
def ideas():
	query= execute_query("""SELECT name, idea_ID FROM Ideas WHERE name is not null and name != '' ORDER BY name ASC""")
	#newlist = unicode_to_html(query)
	return render_template('ideas.html', rows=query)

@app.route('/ideas/<id>', methods=['GET'])
def ideaDescription(id):
	query= execute_query("""SELECT * FROM Ideas WHERE idea_ID = %s""", [id])
	return render_template('idea-description.html')

@app.route('/add/idea-added', methods=['GET', 'POST'])
def ideaAdded():
	""" Adds an idea to the database """
	idea = {
		'title': request.form['title'],
		'category': request.form['category'],
		'description': request.form['description']
	}
	query = execute_query("""INSERT INTO Ideas(name, category, description) VALUES (%s, %s, %s)""", [idea['title'], idea['category'], idea['description']])
	return render_template('idea-added.html')

""" SQL Functions """

@app.route("/viewdb")
def viewdb():
	rows = execute_query("""SELECT * FROM Ideas;""")
	return '<br>'.join(str(row) for row in rows) # Displays everything in db in the browser

# def unicode_to_html(query): 
# 	""" Converts UTF-8 unicode from a query
# 		and converts it to HTML.
# 		@param {query} The query that fetches the rows in unicode (must only be selecting strings)
# 		@return list of the new rows in the table not in unicode
# 	"""
# 	for tup in query:
# 		print tup[1]
# 	newlist = []
# 	for tup in query:
# 		llist = ([str(item).encode('ascii','backslashreplace') for item in tup])
# 		newlist.append(llist)
# 	return newlist


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

if __name__ == '__main__':
  app.run(debug = True)