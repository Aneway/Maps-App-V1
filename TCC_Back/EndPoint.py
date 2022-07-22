from flask import Flask
from flask import request
from flask_cors import CORS
from flask_mysqldb import MySQL
import MySQLdb.cursors
from Services import *

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'boschmaps'
mysql = MySQL(app)

CORS(app)


@app.route('/', methods=['POST'])
def SerachEDV():
    data = request.get_json(force=True)
    return SearchEDV(int(data['EDV']))

@app.route('/register',methods=['POST'])
def registerUsers():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    data = request.get_json(force=True)
    return registerUser(cursor,data)


if __name__ == '__main__':
    app.run(debug=True)
