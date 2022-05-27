from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'phpmyadmin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Secret1'
app.config['MYSQL_DATABASE_DB'] = 'dima_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
