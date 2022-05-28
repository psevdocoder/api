import pymysql
from flask import request, Blueprint

from app import app
from config import mysql
from flask import jsonify
from flask import request


queue = Blueprint('queue', __name__)


@queue.route('/joinqueue', methods=['POST'])
def joinqueue():

    try:
        json = request.json
        fullname = json['fullname']

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)


        # cursor.execute("CREATE TABLE IF NOT EXISTS 'pr_queue' ('id' int(2))")

        # cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'pr_queue'")
        # tab_count = cursor.fetchone().__str__()
        # tab_count = tab_count[-2]
        # table_count = int(tab_count)
        # print(table_count)
        # if table_count < 1:

        cursor.execute("SELECT name FROM dima_table")
        row = cursor.fetchall()
        for lg in row:
            if lg['fullname'] == fullname:
                respone = jsonify("already_in_queuee")
                respone.status_code = 200
                return respone

        sqlquery = "INSERT INTO dima_table(name) VALUES (%s)"
        binddata = fullname
        cursor.execute(sqlquery, binddata)
        conn.commit()
        respone = jsonify("joinedqueue")
        respone.status_code = 200
        return respone


    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()



@queue.route('/leavequeue', methods=['POST'])
def leavequeue():
    try:
        json = request.json
        fullname = json['fullname']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sqlquery = "DELETE FROM dima_table WHERE name=%s"
        binddata = fullname
        cursor.execute(sqlquery, binddata)
        conn.commit()
        respone = jsonify("leftqueue")
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()