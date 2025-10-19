import mysql.connector #import connector i installed in git
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server (adjust credentials if necessary)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure connection is properly closed
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            # Optional message to confirm closure
            # print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
