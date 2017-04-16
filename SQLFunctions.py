from flaskext.mysql import MySQL

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

