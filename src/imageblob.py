from flask import Blueprint

from app import app
from config import mysql
from flask import jsonify
from flask import request
import pymysql


imageblob = Blueprint('imageblob', __name__)




def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

@imageblob.route('/setimage', methods=['POST'])
def insertBLOB():
    json = request.json
    login = json['login']
    binphoto = json['binphoto']

    print("Inserting BLOB into python_employee table")

    try:
        connection = mysql.connect()
        cursor = connection.cursor()
        sql_q = "UPDATE account SET photo=%s WHERE login =%s"

        empPicture = convertToBinaryData(binphoto)

        # Convert data into tuple format
        insert_blob_tuple = (empPicture, login)
        result = cursor.execute(sql_q, insert_blob_tuple)
        connection.commit()
        print("Image inserted successfully as a BLOB into", result)

    except mysql.connect.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        cursor.close()
        connection.close()
        return("MySQL connection is closed")


@imageblob.route('/getimage', methods=['GET'])
def readBLOB():
    login = request.args.get('login')


    print("Reading BLOB data from python_employee table")

    try:
        connection = mysql.connect()
        cursor = connection.cursor()
        sql_fetch_blob_query = "SELECT * from account where login = %s"

        cursor.execute(sql_fetch_blob_query, (login,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            image = row[4]
            print("Storing employee image on disk \n")
            # write_file(image, photo)

    except mysql.connect.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


# def write_file(data, filename):
#     # Convert binary data to proper format and write it on Hard Disk
#     with open(filename, 'wb') as file:
#         file.write(data)