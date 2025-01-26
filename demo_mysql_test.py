import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Admin2002",
  database="mydatabase"
)
print(mydb)

