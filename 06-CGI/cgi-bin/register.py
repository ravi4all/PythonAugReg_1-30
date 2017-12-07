#!C:/Python36/python.exe

import cgi
import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='e_comm', autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()

username = form.getvalue('username')
userpwd = form.getvalue('userpwd')
usermail = form.getvalue('usermail')
usercity = form.getvalue('city')
usergender = form.getvalue('gender')


query = "INSERT INTO users VALUES (%s, %s, %s, %s, %s)"

cursor.execute(query, (username, userpwd, usermail, usercity, usergender))

print("Content-type:text/html\r\n\r\n")
print("""
<html>
<head>
<title>Python</title>
</head>
<body>
<h1>Registered Successfully</h1>
</body>
</html>
""")

