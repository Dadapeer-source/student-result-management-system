import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dadapeer@2005@",
        database="student_result"
    )
