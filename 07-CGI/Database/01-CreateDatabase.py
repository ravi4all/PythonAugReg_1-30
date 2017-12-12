import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='demo_1', autocommit=True)

cursor = connection.cursor()

cursor.execute(query="CREATE TABLE users_1 (Name TEXT(50), Email VARCHAR(50), Password VARCHAR(50))")

print("Table Created Successfully...")
