from flaskext.mysql import MySQL
from flask import Flask

connection = Flask(__name__)

connection.config['MYSQL_DATABASE_HOST'] = 'localhost'
connection.config['MYSQL_DATABASE_PORT'] = 3306
connection.config['MYSQL_DATABASE_USER'] = 'root'
connection.config['MYSQL_DATABASE_PASSWORD'] = 'Abc123*'
connection.config['MYSQL_DATABASE_DB'] = 'users'

mysql = MySQL(connection)

