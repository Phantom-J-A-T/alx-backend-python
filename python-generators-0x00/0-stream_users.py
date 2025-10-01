#!/usr/bin/python3
"""
Generator that streams rows from user_data table one by one
"""

import mysql.connector


def stream_users():
    """
    Generator function that yields rows from user_data table
    one at a time as dictionaries
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",       # adjust credentials if needed
            password="root",   # adjust credentials if needed
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
