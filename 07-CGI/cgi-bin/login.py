#!C:/Python36/python.exe

import cgi
import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='pythonregistration', autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()

usermail = form.getvalue('usermail')
userPwd = form.getvalue('userpwd')

# usermail = "ravi@gmail.com"
# userPwd = "ravi123"

def printHtml(data):
    print("Content-type:text/html\r\n\r\n")
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    """)

    if usermail and userPwd in data:
        print("""
    <h1>Welcome to python CGI</h1>
    <h2>Name is {}</h2>
    <h2>Email is {}</h2>
    <h2>Country is {}</h2>
    <h2>Gender is {}</h2>
    <a href="../homePage.html">Home</a>
    <a href="../changePassword.html">Change Password</a>
    """.format(data[0], data[1], data[3], data[4]))
    else:
        print("""
    <h1>Login Failed</h1>
    <a href="../homePage.html">Home</a>
    """)

    print("""
    </body>
    </html>
    """)


def loginUser():
    data = ()
    query = "SELECT * FROM users WHERE UserEmail = %s AND UserPwd = %s"

    cursor.execute(query, (usermail, userPwd))
    # for d in cursor:
    #     data.append(d)

    try:
        for d in cursor:
            data = d
        printHtml(data)
    except Exception as ex:
        print("Exception...",ex)

    # registerhtml(d)

loginUser()
