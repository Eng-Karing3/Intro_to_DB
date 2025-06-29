import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (change password if needed)
        connection = mysql.connector.connect(
            host='DEVELOPER',
            user='root',
            password=''  # ← replace this
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as err:
        print(f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
