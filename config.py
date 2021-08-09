from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'g573333'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'avs'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)
