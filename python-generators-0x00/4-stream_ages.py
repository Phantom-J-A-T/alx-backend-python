#!/usr/bin/python3
"""
Memory-efficient average age computation using generators
"""

import seed


def stream_user_ages():
    """
    Generator that yields user ages one by one from user_data
    """
    connection = None
    cursor = None
    try:
        connection = seed.connect_to_prodev()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT age FROM user_data")

        for row in cursor:   # loop 1
            yield row["age"]

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def compute_average_age():
    """
    Compute average age using the generator without
    loading entire dataset into memory
    """
    total, count = 0, 0
    for age in stream_user_ages():  # loop 2
        total += age
        count += 1

    avg = total / count if count else 0
    print(f"Average age of users: {avg:.2f}")


if __name__ == "__main__":
    compute_average_age()
