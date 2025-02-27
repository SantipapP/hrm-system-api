import mysql.connector
from mysql.connector import Error

def hrm_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",       # เปลี่ยนเป็นชื่อโฮสต์ของคุณ
            user="root",   # เปลี่ยนเป็นชื่อผู้ใช้ของคุณ
            password="", # เปลี่ยนเป็นรหัสผ่านของคุณ
            database="hrm-system-db"  # เปลี่ยนเป็นชื่อฐานข้อมูลของคุณ
        )
        if connection.is_connected():
            print("Connection to MySQL was successful!")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None