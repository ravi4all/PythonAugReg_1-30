#!C:/Python36/python.exe

import cgi

form = cgi.FieldStorage()

name = form.getvalue('username')
pwd = form.getvalue('userpwd')

def loginCheck():
    if name == pwd:
        return "Hello "+name
    else:
        return "You are not registered"

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
""".format(loginCheck()))
