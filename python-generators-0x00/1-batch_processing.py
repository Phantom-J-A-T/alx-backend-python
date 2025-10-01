#!/usr/bin/python3
"""
Batch processing generator for user_data table
"""

import mysql.connector


def stream_users_in_batches(batch_size):
    """
    Generator that fetches rows in batches from user_data
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
        while True:
            rows = cursor.fetchmany(batch_size)
            if not rows:
                break
            yield rows
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def batch_processing(batch_size):
    """
    Processes batches: filter users with age > 25
    and prints them row by row
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user["age"] > 25:
                print(user)
