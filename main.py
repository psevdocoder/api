import datetime
import pymysql

from app import app
from config import mysql
from flask import jsonify
from flask import request


#test
@app.route('/create', methods=['POST'])
def create_emp():
    try:
        _json = request.json
        _name = _json['name']
        _email = _json['email']
        _phone = _json['phone']
        _address = _json['address']
        if _name and _email and _phone and _address and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO emp(name, email, phone, address) VALUES(%s, %s, %s, %s)"
            bindData = (_name, _email, _phone, _address)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Employee added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#test
@app.route('/emp')
def emp():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name, email, phone, address FROM emp")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#test
@app.route('/emp/<int:emp_id>')
def emp_details(emp_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name, email, phone, address FROM emp WHERE id =%s", emp_id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#test
@app.route('/update', methods=['PUT'])
def update_emp():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _email = _json['email']
        _phone = _json['phone']
        _address = _json['address']
        if _name and _email and _phone and _address and _id and request.method == 'PUT':
            sqlQuery = "UPDATE emp SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
            bindData = (_name, _email, _phone, _address, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Employee updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#test
@app.route('/delete/', methods=['DELETE'])
def delete_emp(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM emp WHERE id =%s", (id,))
        conn.commit()
        respone = jsonify('Employee deleted successfully!')
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone


@app.route('/register', methods=['POST'])
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
                    respone = jsonify("not_added")
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


@app.route('/command', methods=['POST'])
def command():
    _json = request.json
    _command = _json['command']
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(_command)
        # cursor.execute("SELECT id, fullname FROM account WHERE login='"+login+"' AND password='"+password+"'")
        conn.commit()

        respone = jsonify("command executed check changes in database, dim-dim")
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/login', methods=['POST'])
def login():
    json = request.json
    login = json['login']
    password = json['password']

    # print(login, password)
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, fullname FROM account WHERE login='"+login+"' AND password='"+password+"'")
        # cursor.execute("SELECT id, fullname, login, password FROM account WHERE login='" + login + "'")
        row = cursor.fetchone()
        respone = jsonify(row)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()





#Getter by login
@app.route('/getlogin', methods=['GET'])
def password():
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
@app.route('/getpassword', methods=['GET'])
def getpassword():
    password = request.args.get('password')
    # print(login, password)
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # cursor.execute("SELECT id, fullname FROM account WHERE login='"+login+"' AND password='"+password+"'")
        cursor.execute("SELECT id, fullname, login, password FROM account WHERE password='" + password + "'")
        Row = cursor.fetchone()
        respone = jsonify(Row)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#Getter by id
@app.route('/getid', methods=['GET'])
def id():
    id = request.args.get('id')
    # password = request.args.get('password')
    # print(login, password)
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # cursor.execute("SELECT id, fullname FROM account WHERE login='"+login+"' AND password='"+password+"'")
        cursor.execute("SELECT id, fullname, login, password FROM account WHERE id='" + id + "'")
        Row = cursor.fetchone()
        respone = jsonify(Row)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#Getter by fullname
@app.route('/getfullname', methods=['GET'])
def fullname():
    fullname = request.args.get('fullname')
    # password = request.args.get('password')
    # print(login, password)
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # cursor.execute("SELECT id, fullname FROM account WHERE login='"+login+"' AND password='"+password+"'")
        cursor.execute("SELECT id, fullname, login, password FROM account WHERE fullname='" + fullname + "'")
        Row = cursor.fetchone()
        respone = jsonify(Row)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/newpoll', methods=['POST'])
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




# #Фоновая задача для своевременного удаления неактуальных опросов
# def check_time_to_die():
#     with app.app_context():
#         while True:
#             conn = mysql.connect()
#             cursor = conn.cursor(pymysql.cursors.DictCursor)
#             cursor.execute("SELECT id, subject, timetodie FROM polls")
#             empRow = cursor.fetchone()
#             respone = jsonify(empRow)
#             respone.status_code = 200
#             print(empRow)
#             time.sleep(5)
#             # return respone
#
#
# thread = Thread(target=check_time_to_die)
# thread.start()






if __name__ == "__main__":
    app.run(debug=True)
