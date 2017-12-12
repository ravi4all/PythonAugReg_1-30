import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='pythonregistration', autocommit=True)

cursor = connection.cursor()

userEmail = input("Enter your mail : ")
userPwd = input("Enter your pwd : ")

# cursor.execute(query="INSERT INTO user_1 VALUES('Ram', 'ram@gmail.com', 'ram12345')")

query = "SELECT * FROM user_1 WHERE Email = %s AND Password = %s"

cursor.execute(query, (userEmail, userPwd))

for i in cursor:
    print(i)

try:
    if userEmail and userPwd in i:
        print("Hello {}".format(i[0]))
    # elif userEmail and userPwd not in i:
    #     print("Register First")

except Exception as err:
    print("Login Failed...")

