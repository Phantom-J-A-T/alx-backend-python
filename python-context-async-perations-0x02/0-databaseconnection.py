#!/usr/bin/env python3
import sqlite3


class DatabaseConnection:
    """Custom context manager for handling SQLite DB connections"""

    def __init__(self, db_name="users.db"):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        # Open connection
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        # Ensure connection is closed properly
        if self.conn:
            self.conn.close()
        # Returning False means exceptions (if any) will not be suppressed
        return False


if __name__ == "__main__":
    # Use the context manager to run a query
    with DatabaseConnection("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        print(results)
