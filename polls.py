from flask import Blueprint

from app import app
from config import mysql
from flask import jsonify
from flask import request
import datetime
import pymysql

polls = Blueprint('polls', __name__)


@polls.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone


@polls.route('/newpoll', methods=['POST'])
def newpoll():
    try:
        _json = request.json
        _subject = _json['subject']
        _time = _json['time'] #Время жизни

        _timestamp = datetime.datetime.now() # Текущее время
        _timetostop = _time + _timestamp #Время конца жизни строчки



        if _subject and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)


            sqlQuery = "INSERT INTO polls(subject, timetostop) VALUES(%s, %s)"
            bindData = (_subject, _timetostop)
            cursor.execute(sqlQuery, bindData)
            conn.commit()

            respone = jsonify('Poll added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()