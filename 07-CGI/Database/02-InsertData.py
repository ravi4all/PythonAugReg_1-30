import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='pythonregistration', autocommit=True)

cursor = connection.cursor()

userName = input("Enter your name : ")
userEmail = input("Enter your mail : ")
userPwd = input("Enter your pwd : ")

# cursor.execute(query="INSERT INTO user_1 VALUES('Ram', 'ram@gmail.com', 'ram12345')")

query = "INSERT INTO user_1 VALUES(%s, %s, %s)"

cursor.execute(query, (userName, userEmail, userPwd))

print("Data Inserted Successfully...")
