from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'S3cret'
app.config['MYSQL_DATABASE_DB'] = 'project'
app.config['MYSQL_DATABASE_HOST'] = '185.18.55.107'
mysql.init_app(app)
