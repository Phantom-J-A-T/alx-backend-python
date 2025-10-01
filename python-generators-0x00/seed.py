#!/usr/bin/python3
"""
Seed script for MySQL database ALX_prodev
"""

import mysql.connector
from mysql.connector import errorcode
import csv


def connect_db():
    """
    Connect to MySQL server (without specifying database)
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # adjust if needed
            password="root"     # adjust if needed
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_database(connection):
    """
    Create ALX_prodev database if it does not exist
    """
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")


def connect_to_prodev():
    """
    Connect to ALX_prodev database
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",       # adjust if needed
            password="root",   # adjust if needed
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_table(connection):
    """
    Create user_data table if not exists
    """
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL,
                INDEX(user_id)
            )
        """)
        connection.commit()
        cursor.close()
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")


def insert_data(connection, filename):
    """
    Insert data from CSV file into user_data table if not exists
    """
    try:
        cursor = connection.cursor()
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                cursor.execute("""
                    SELECT user_id FROM user_data WHERE user_id = %s
                """, (row["user_id"],))
                exists = cursor.fetchone()
                if not exists:
                    cursor.execute("""
                        INSERT INTO user_data (user_id, name, email, age)
                        VALUES (%s, %s, %s, %s)
                    """, (row["user_id"], row["name"], row["email"], row["age"]))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Error inserting data: {e}")
