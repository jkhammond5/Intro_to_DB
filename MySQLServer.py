import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Step 1: Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",      # or your server IP
            user="root",           # replace with your MySQL username
            password="Realities24!"  # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Step 2: Create database if it doesn’t exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Step 3: Close cursor and connection safely
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
