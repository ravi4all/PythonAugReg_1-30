import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='e_comm', autocommit=True)

cursor = connection.cursor()

prod_name = input("Enter name of product : ")
prod_price = int(input("Enter price of product : "))
prod_brand = input("Enter brand of product : ")

# query = "INSERT INTO products VALUES ('Note 4', 12000, 'Redmi')"

query = "INSERT INTO products VALUES (%s, %s, %s)"

cursor.execute(query, (prod_name, prod_price, prod_brand))
