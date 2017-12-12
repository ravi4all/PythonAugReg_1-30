#!C:/Python36/python.exe

import cgi
import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='pythonregistration', autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()

username = form.getvalue('username')
userPwd = form.getvalue('userpwd')
usermail = form.getvalue('usermail')
usercountry = form.getvalue('country')
usergender = form.getvalue('gender')


# def login():
#     if username == userPwd:
#         return "Login Successfull " + username
#     else:
#         return "Login Failed"


def registerhtml():
    print("Content-type:text/html\r\n\r\n")
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <h1>Welcome to python CGI</h1>
    <h2>Name is {}</h2>
    <h2>Email is {}</h2>
    <h2>Country is {}</h2>
    <h2>Gender is {}</h2>
    </body>
    </html>
    """.format(username, usermail, usercountry, usergender))

def registerUser():
    query = "INSERT INTO users VALUES(%s, %s, %s, %s, %s)"

    cursor.execute(query, (username, usermail, userPwd, usercountry, usergender))

    registerhtml()

registerUser()
