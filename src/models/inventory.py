# models/inventory.py
# Manages the collection of products.

from .product import Product
# The import is now from the database module instead of the api client
from db.database import fetch_all_products_from_db, update_stock_in_db

class Inventory:
    """
    Manages a dictionary of products, indexed by product_id.
    """
    def __init__(self):
        """
        Initializes the Inventory, starting with an empty product list
        and fetching initial data from the database.
        """
        self._products = {}
        self.load_products_from_db()

    def load_products_from_db(self):
        """
        Fetches product data from the database and populates the inventory.
        """
        print("Loading product list from the database...")
        product_list_from_db = fetch_all_products_from_db()
        
        self._products.clear() # Clear existing data before loading new data
        
        if product_list_from_db:
            for item in product_list_from_db:
                try:
                    product = Product(
                        product_id=item.get('id'),
                        name=item.get('name'),
                        price=item.get('price'),
                        stock=item.get('stock')
                    )
                    self._products[product.product_id] = product
                except (ValueError, TypeError) as e:
                    print(f"Skipping invalid product data: {item}. Error: {e}")
            print(f"Successfully loaded {len(self._products)} products from the database.")
        else:
            print("Could not fetch product data or no products available in the database.")


    def add_stock(self, product_id, quantity):
        """
        Adds a specified quantity to a product's stock and updates the database.

        Args:
            product_id (str): The ID of the product to update.
            quantity (int): The amount of stock to add.

        Raises:
            KeyError: If the product_id does not exist.
            ValueError: If the update operation fails.
        """
        product_id = str(product_id)
        if product_id in self._products:
            product = self._products[product_id]
            try:
                # First, update the object in memory
                original_stock = product.stock
                product.update_stock(quantity)
                
                # Then, persist the change to the database
                if update_stock_in_db(product_id, product.stock):
                    print(f"Database updated for product {product_id}.")
                else:
                    # If DB update fails, revert the change in memory
                    product.stock = original_stock
                    raise ValueError(f"Failed to update stock in database for product {product_id}.")

            except ValueError as e:
                # Re-raise the exception to be handled by the caller
                raise e
        else:
            raise KeyError(f"Product with ID '{product_id}' not found in inventory.")

    def get_product(self, product_id):
        """
        Retrieves a single product by its ID.

        Args:
            product_id (str): The ID of the product to retrieve.

        Returns:
            Product: The product object, or None if not found.
        """
        return self._products.get(str(product_id))

    def get_all_products(self):
        """
        Returns a list of all products in the inventory.

        Returns:
            list: A list of Product objects.
        """
        return list(self._products.values())
