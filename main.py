from src.accounts import accounts
from src.polls import polls
from src.imageblob import imageblob
from src.example import example

from app import app

# @app.route('/command', methods=['POST'])
# def command():
#     _json = request.json
#     _command = _json['command']
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         cursor.execute(_command)
#         # cursor.execute("SELECT id, fullname FROM account WHERE login='"+login+"' AND password='"+password+"'")
#         conn.commit()
#
#         respone = jsonify("command executed check changes in database, dim-dim")
#         respone.status_code = 200
#         return respone
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()


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



app.register_blueprint(accounts)
app.register_blueprint(polls)
app.register_blueprint(imageblob)
app.register_blueprint(example)



if __name__ == "__main__":
    app.run(debug=True)
