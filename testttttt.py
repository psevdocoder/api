import mysql.connector
from flask import request

from app import app
from config import mysql
from flask import jsonify
from flask import request



def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
        print(binaryData)
    return binaryData


def insertBLOB(login, photo):
    # json = request.json
    # login = json['login']
    # binphoto = json['binphoto']

    print("Inserting BLOB into python_employee table")

    try:
        connection = mysql.connect()
        cursor = connection.cursor()
        sql_q = "UPDATE account SET photo=%s WHERE login =%s"

        empPicture = convertToBinaryData(photo)

        # Convert data into tuple format
        insert_blob_tuple = (empPicture, login)
        result = cursor.execute(sql_q, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connect.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        cursor.close()
        connection.close()
        print("MySQL connection is closed")



def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)



insertBLOB("p", "C:/Users/Maksim/Desktop/qwerty.png")




# def readBLOB(id, photo):


#     print("Reading BLOB data from python_employee table")

#     try:
#         connection = mysql.connect()
#         cursor = connection.cursor()
#         sql_fetch_blob_query = "SELECT * from account where id = %s"

#         cursor.execute(sql_fetch_blob_query, (id,))
#         record = cursor.fetchall()
#         for row in record:
#             print("Id = ", row[0], )
#             print("Name = ", row[1])
#             image = row[4]
#             print("Storing employee image on disk \n")
#             write_file(image, photo)

#     except mysql.connect.Error as error:
#         print("Failed to read BLOB data from MySQL table {}".format(error))

#     finally:
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")


# readBLOB(85, "2222.png")