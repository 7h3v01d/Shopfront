# main.py
# This is the main entry point for the inventory management application.

import os
import time
from datetime import datetime

# Local application imports
from models.inventory import Inventory
from utils.formatter import format_currency
from db.database import initialize_database # New import

def clear_screen():
    """Clears the console screen."""
    # A simple cross-platform way to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

def display_inventory(inventory):
    """
    Displays the current inventory in a formatted table.
    
    Args:
        inventory (Inventory): The inventory object to display.
    """
    print("=============================================")
    print(f"    Inventory Report as of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=============================================")
    print(f"{'ID':<5} {'Product Name':<20} {'Price':<10} {'Stock':<5}")
    print("---------------------------------------------")

    products = inventory.get_all_products()
    if not products:
        print("No products in inventory.")
    else:
        for product in products:
            price_str = format_currency(product.price)
            print(f"{product.product_id:<5} {product.name:<20} {price_str:<10} {product.stock:<5}")
    
    print("=============================================\n")


def main():
    """
    Main function to run the application.
    """
    clear_screen()
    print("Initializing Inventory Management System...")
    
    # Initialize the database (creates table and seeds data if needed)
    initialize_database()
    
    # Create an inventory instance which now loads from DB
    inventory = Inventory()
    
    print("System ready.")
    time.sleep(2) # Simulate some work
    
    clear_screen()
    
    # Main application loop
    while True:
        display_inventory(inventory)
        print("Options:")
        print("1. Refresh product data from database")
        print("2. Add stock to a product")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("Refreshing data from database...")
            inventory.load_products_from_db()
            time.sleep(1)
            clear_screen()
        elif choice == '2':
            product_id = input("Enter product ID to add stock: ")
            try:
                quantity = int(input("Enter quantity to add: "))
                inventory.add_stock(product_id, quantity)
                print(f"Added {quantity} to product {product_id}.")
            except ValueError as e:
                print(f"Error: {e}")
            except KeyError:
                print(f"Product with ID '{product_id}' not found.")
            time.sleep(2)
            clear_screen()
        elif choice == '3':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)
            clear_screen()

if __name__ == "__main__":
    main()
