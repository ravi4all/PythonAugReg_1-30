import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='e_comm', autocommit=True)

cursor = connection.cursor()

query = "CREATE TABLE products (Name VARCHAR(50), Price INT(255), Brand VARCHAR(50))"

cursor.execute(query)
