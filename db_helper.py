import pymysql
conn = pymysql.Connect(host='localhost',
    user='root',
    password='POLICE',
    database='expense_manager')


import mysql.connector
print('working')
# connection = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='POLICE',
#     database='expense_manager'
# )
#connection.is_connected()
    

cursor = conn.cursor()
cursor.execute("SELECT * FROM expenses WHERE amount= 50")
expenses = cursor.fetchall()
for expens in expenses:
    print(expens)
conn.close()
print('running')