import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='e_comm', autocommit=True)

cursor = connection.cursor()

query = "SELECT * FROM products WHERE Name = %s"

cursor.execute(query, ('V7'))

for i in cursor:
    print(i)
