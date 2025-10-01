#!/usr/bin/env python3
import sqlite3


class ExecuteQuery:
    """Custom context manager that executes a query and returns results"""

    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params if params is not None else ()
        self.conn = None
        self.cursor = None
        self.results = None

    def __enter__(self):
        # Open DB connection
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        # Execute the query
        self.cursor.execute(self.query, self.params)
        self.results = self.cursor.fetchall()

        return self.results

    def __exit__(self, exc_type, exc_value, traceback):
        # Clean up resources
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        # Do not suppress exceptions
        return False


if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)

    with ExecuteQuery("users.db", query, params) as results:
        print(results)
