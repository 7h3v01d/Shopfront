# db/database.py
# Handles all database interactions for the application.

import sqlite3
from config import app_config

def get_db_connection():
    """
    Establishes a connection to the SQLite database.
    The connection object will allow row objects to be accessed by column name.
    """
    try:
        conn = sqlite3.connect(app_config.DATABASE_URI.split('///')[1])
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def initialize_database():
    """
    Initializes the database with the required 'products' table and seeds it
    with some initial data if the table doesn't exist.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Check if the table already exists
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
            if cursor.fetchone() is None:
                print("Creating 'products' table...")
                cursor.execute("""
                    CREATE TABLE products (
                        id TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        price REAL NOT NULL,
                        stock INTEGER NOT NULL
                    )
                """)
                # Seed the table with some initial data
                print("Seeding database with initial data...")
                seed_data = [
                    ('101', 'Laptop', 1200.50, 15),
                    ('102', 'Mouse', 25.00, 120),
                    ('103', 'Keyboard', 75.99, 75),
                    ('201', 'Monitor', 300.00, 30),
                    ('205', 'Webcam', 50.25, 50),
                ]
                cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?)", seed_data)
                conn.commit()
                print("Database initialized and seeded.")
            else:
                print("Database already initialized.")
        except sqlite3.Error as e:
            print(f"An error occurred during database initialization: {e}")
        finally:
            conn.close()

def fetch_all_products_from_db():
    """
    Fetches all products from the database.

    Returns:
        list: A list of dictionaries representing the products, or an empty list on error.
    """
    conn = get_db_connection()
    products = []
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products")
            rows = cursor.fetchall()
            # Convert row objects to dictionaries
            products = [dict(row) for row in rows]
        except sqlite3.Error as e:
            print(f"Failed to fetch products from database: {e}")
        finally:
            conn.close()
    return products

def update_stock_in_db(product_id, new_stock_level):
    """
    Updates the stock level for a specific product in the database.

    Args:
        product_id (str): The ID of the product to update.
        new_stock_level (int): The new stock quantity.
    
    Returns:
        bool: True if the update was successful, False otherwise.
    """
    conn = get_db_connection()
    success = False
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (new_stock_level, product_id))
            conn.commit()
            if cursor.rowcount > 0:
                success = True
        except sqlite3.Error as e:
            print(f"Failed to update stock for product {product_id}: {e}")
        finally:
            conn.close()
    return success
