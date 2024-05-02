import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='lentopeli',
    user='root',
    password='Khanhdung1509',
    autocommit=True
)
