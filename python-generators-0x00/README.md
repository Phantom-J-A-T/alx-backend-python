# Python Generators - Database Seeder

This project seeds a MySQL database (`ALX_prodev`) with user data from a CSV file.

## Features
- Connects to MySQL server
- Creates `ALX_prodev` database if not present
- Creates `user_data` table if not present
- Inserts data from `user_data.csv` (skips duplicates)

## Table Schema
- **user_id** (UUID, Primary Key, Indexed)
- **name** (VARCHAR, NOT NULL)
- **email** (VARCHAR, NOT NULL)
- **age** (DECIMAL, NOT NULL)

## Usage
```bash
chmod +x 0-main.py
./0-main.py
