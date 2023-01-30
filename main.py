import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'projetobdcrud',
)

cursor = connection.cursor()

# code here




# end code

cursor.close()
connection.close()
