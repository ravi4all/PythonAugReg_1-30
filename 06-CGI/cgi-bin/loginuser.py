#!C:/Python36/python.exe

import cgi
import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='e_comm', autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()

usermail = form.getvalue('username')
userpwd = form.getvalue('userpwd')

def loginCheck():
    query = "SELECT * FROM users WHERE Email = %s AND Password = %s"
    cursor.execute(query, (usermail, userpwd))
    for i in cursor:
        pass
    printUser(i)

def printUser(data):
    print("Content-type:text/html\r\n\r\n")
    print("""
    <html>
    <head>
    <title>Python</title>
    </head>
    <body>
    <h1>{}</h1>
    </body>
    </html>
    """.format(data))

loginCheck()
