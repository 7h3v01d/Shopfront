# models/product.py
# Defines the Product data model.

class Product:
    """
    Represents a single product in the inventory.
    """
    def __init__(self, product_id, name, price, stock):
        """
        Initializes a Product instance.

        Args:
            product_id (str): The unique identifier for the product.
            name (str): The name of the product.
            price (float): The price of the product.
            stock (int): The available quantity in stock.
        """
        if not all([product_id, name]):
            raise ValueError("Product ID and Name cannot be empty.")
        if price < 0 or stock < 0:
            raise ValueError("Price and stock cannot be negative.")
            
        self.product_id = str(product_id)
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def __repr__(self):
        """
        Provides a developer-friendly string representation of the product.
        """
        return (f"Product(id='{self.product_id}', name='{self.name}', "
                f"price={self.price}, stock={self.stock})")

    def update_stock(self, quantity):
        """
        Updates the stock level of the product.

        Args:
            quantity (int): The number of items to add to the stock. 
                            Can be negative to reduce stock.
        """
        new_stock = self.stock + quantity
        if new_stock < 0:
            raise ValueError("Stock level cannot go below zero.")
        self.stock = new_stock
