import mysql.connector

conexion = mysql.connector.connect(user='root', password='orellano',
                                                host='localhost',
                                                database='pruebabd',
                                                port='3306')

print(conexion)
