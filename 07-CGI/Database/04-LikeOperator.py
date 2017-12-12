import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='pythonregistration', autocommit=True)

cursor = connection.cursor()

userEmail = '.com'

query = "SELECT * FROM user_1 WHERE Email LIKE %s"

cursor.execute(query, ('%' + userEmail + '%'))

for i in cursor:
    print(i)

# try:
#     print("Hello {}".format(i[0]))
#
# except Exception as err:
#     print("Login Failed...")

