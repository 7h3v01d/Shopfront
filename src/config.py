# config.py
# Stores configuration variables for the application.

# The endpoint for the product data API.
# This is a dummy URL for demonstration purposes.
API_ENDPOINT = "https://api.example.com/products"

# Other potential configurations could go here
# For example:
# DATABASE_URI = "sqlite:///inventory.db"
# LOG_LEVEL = "INFO"

# config.py
# Stores configuration variables for the application.

import os

class Config:
    """Base configuration class with shared settings."""
    # A secret key might be used for signing data in a web context
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-key'
    
    # API settings
    API_TIMEOUT_SECONDS = 15 # Default request timeout

class DevelopmentConfig(Config):
    """Configuration settings for the development environment."""
    DEBUG = True
    API_ENDPOINT = "https://api.dev.example.com/products"
    LOG_LEVEL = "DEBUG"
    DATABASE_URI = "sqlite:///inventory_dev.db"

class ProductionConfig(Config):
    """Configuration settings for the production environment."""
    DEBUG = False
    API_ENDPOINT = "https://api.example.com/products"
    LOG_LEVEL = "INFO"
    # In production, you'd likely get the database URI from an environment variable
    DATABASE_URI = os.environ.get('DATABASE_URI') or "postgresql://produser:password@dbhost/inventory"

def get_config():
    """
    Returns the appropriate configuration object based on the APP_ENV environment variable.
    Defaults to DevelopmentConfig if the variable is not set.
    """
    env = os.environ.get('APP_ENV', 'development').lower()
    if env == 'production':
        return ProductionConfig()
    return DevelopmentConfig()

# The application can import this 'app_config' object to access settings
app_config = get_config()

# Example of how to use it in another file:
# from config import app_config
# print(f"Connecting to API at: {app_config.API_ENDPOINT}")
