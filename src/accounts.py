from flask import Blueprint

from app import app
from config import mysql
from flask import jsonify
from flask import request
import pymysql



accounts = Blueprint('accounts', __name__)


@accounts.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone


@accounts.route('/register', methods=['POST'])
def register():
    try:
        json = request.json
        fullname = json['fullname']
        login = json['login']
        password = json['password']
        if fullname and login and password and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            #Начало проверки на существование логина
            cursor.execute("SELECT login FROM account")
            row = cursor.fetchall()
            for lg in row:
                #Если такой логин существует то идет ответ: There is already account with such login
                if lg['login'] == login:
                    respone = jsonify("already_have")
                    respone.status_code = 200
                    return respone

            # Иначе создается запись
            sqlQuery = "INSERT INTO account(fullname, login, password) VALUES(%s, %s, %s)"
            bindData = (fullname, login, password)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('added')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#Getter by login
@accounts.route('/login', methods=['GET'])
def login():
    login = request.args.get('login')
    # print(login, password)
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # cursor.execute("SELECT id, fullname FROM account WHERE login='"+login+"' AND password='"+password+"'")
        cursor.execute("SELECT id, fullname, login, password FROM account WHERE login='" + login + "'")
        Row = cursor.fetchone()
        respone = jsonify(Row)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#Getter by password
# @accounts.route('/password', methods=['GET'])
# def password():
#     password = request.args.get('password')
#     # print(login, password)
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         # cursor.execute("SELECT id, fullname FROM account WHERE login='"+login+"' AND password='"+password+"'")
#         cursor.execute("SELECT id, fullname, login, password FROM account WHERE password='" + password + "'")
#         Row = cursor.fetchone()
#         respone = jsonify(Row)
#         respone.status_code = 200
#         return respone
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()



#Getter by id
# @accounts.route('/id', methods=['GET'])
# def id():
#     id = request.args.get('id')
#     # password = request.args.get('password')
#     # print(login, password)
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         # cursor.execute("SELECT id, fullname FROM account WHERE login='"+login+"' AND password='"+password+"'")
#         cursor.execute("SELECT id, fullname, login, password FROM account WHERE id='" + id + "'")
#         Row = cursor.fetchone()
#         respone = jsonify(Row)
#         respone.status_code = 200
#         return respone
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()
#
#
# #Getter by fullname
# @accounts.route('/fullname', methods=['GET'])
# def fullname():
#     fullname = request.args.get('fullname')
#     # password = request.args.get('password')
#     # print(login, password)
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         # cursor.execute("SELECT id, fullname FROM account WHERE login='"+login+"' AND password='"+password+"'")
#         cursor.execute("SELECT id, fullname, login, password FROM account WHERE fullname='" + fullname + "'")
#         Row = cursor.fetchone()
#         respone = jsonify(Row)
#         respone.status_code = 200
#         return respone
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()