import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="joao",
    password="joao",
    database="mysql",
    ssl_disabled=True
)

cursor = conn.cursor()
cursor.execute("SELECT db FROM db;")
for linha in cursor:
    print(linha)

