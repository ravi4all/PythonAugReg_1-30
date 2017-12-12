#!C:/Python36/python.exe

import cgi
import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='pythonregistration', autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()

usermail = form.getvalue('useremail')
oldPwd = form.getvalue('oldPwd')
newPwd = form.getvalue('newPwd')

# usermail = 'vaibhav@gmail.com'
# oldPwd = 'vaibhav909090'
# newPwd = 'vaibhav1234'

def printHtml(name):
    print("Content-type:text/html\r\n\r\n")
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <h1>Query executed for {} {}</h1>
    <h1>Password Updated Successfully for {}</h1>
    </body>
    </html>
    """.format(usermail, oldPwd, name))

def updatePassword():
    data = ()
    query = "UPDATE users SET UserPwd = %s WHERE UserEmail = %s AND UserPwd = %s"

    cursor.execute(query, (newPwd, usermail, oldPwd))

    query_1 = "SELECT * FROM users WHERE UserEmail = %s AND UserPwd = %s"
    cursor.execute(query_1, (usermail, newPwd))

    for d in cursor:
        print("Data -",d)
        data = d

    printHtml(data)

updatePassword()
