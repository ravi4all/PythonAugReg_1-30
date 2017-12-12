#!C:/Python36/python.exe

import cgi
import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='jobs', autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()

searchVal = form.getvalue('searchVal')
location = form.getvalue('location')

# searchVal = 'Software'

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
    <h1>Welcome to python CGI</h1>
    <h2>Job Found</h2>
    <div>{}</div>
    </body>
    </html>
    """.format(data))


def loginUser():
    data = []
    query = "SELECT * FROM jobs WHERE JobTitle LIKE %s OR CompanyName LIKE %s OR Skills LIKE %s"

    cursor.execute(query, ('%' + searchVal + '%','%' + searchVal + '%','%' + searchVal + '%'))
    # for d in cursor:
    #     data.append(d)

    try:
        for d in cursor:
            data.append(d)
        printHtml(data)
    except Exception as ex:
        print("Exception...",ex)

    # registerhtml(d)

loginUser()
