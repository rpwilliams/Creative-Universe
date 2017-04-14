from flask import Flask, render_template, url_for
from flaskext.mysql import MySQL

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'tOrpedo02'
app.config['MYSQL_DATABASE_DB'] = 'Ideas'
app.config['MYSQL_DATABASE_HOST'] = 'rpwilliams96-desktop'
mysql.init_app(app)

app = Flask(__name__)
mysql = MySQL()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
	return render_template('add.html')

@app.route('/ideas', methods=['GET', 'POST'])
def ideas():
	return render_template('ideas.html')

if __name__ == '__main__':
  app.run(debug = True)