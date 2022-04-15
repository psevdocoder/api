import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

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

#needed
@app.route('/register', methods=['POST'])
def register():
    try:
        _json = request.json
        _fullname = _json['fullname']
        _login = _json['login']
        _password = _json['password']
        if _fullname and _login and _password and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO account(fullname, login, password) VALUES(%s, %s, %s)"
            bindData = (_fullname, _login, _password)
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


#needed, doesn't work yet
@app.route('/login', methods=['GET'])
def login():
    login = request.args.get('login')
    password = request.args.get('password')
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


#needed, doesn't work yet
@app.route('/password', methods=['GET'])
def password():
    password = request.args.get('password')
    # password = request.args.get('password')
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


#needed, doesn't work yet
@app.route('/id', methods=['GET'])
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


#needed, doesn't work yet
@app.route('/fullname', methods=['GET'])
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


# #needed, doesn't work yet
# @app.route('/login/<email>', methods=['GET'])
# def login(email):
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         cursor.execute("SELECT id, fullname FROM account WHERE email =%s", email)
#         Row = cursor.fetchone()
#         respone = jsonify(Row)
#         respone.status_code = 200
#         return respone
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()


if __name__ == "__main__":
    app.run(debug=True)