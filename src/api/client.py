# api/client.py
# Simulates fetching data from an external API.

import requests
import json
from config import API_ENDPOINT

def fetch_product_data():
    """
    Fetches product data from a simulated API endpoint.
    In a real application, this would make a network request.
    Here, we simulate it to avoid actual network dependency for this example.

    Returns:
        list: A list of dictionaries, where each dictionary represents a product.
              Returns None if the request fails.
    """
    try:
        # In a real scenario, you would use requests like this:
        # response = requests.get(API_ENDPOINT, timeout=10)
        # response.raise_for_status()  # Raises an HTTPError for bad responses
        # return response.json()

        # For this test program, we'll simulate the response to avoid failure
        # if the endpoint is not available or if requests is not installed.
        print(f"Simulating API call to {API_ENDPOINT}")
        mock_response_data = [
            {'id': 101, 'name': 'Laptop', 'price': 1200.50, 'stock': 15},
            {'id': 102, 'name': 'Mouse', 'price': 25.00, 'stock': 120},
            {'id': 103, 'name': 'Keyboard', 'price': 75.99, 'stock': 75},
            {'id': 201, 'name': 'Monitor', 'price': 300.00, 'stock': 30},
            {'id': 205, 'name': 'Webcam', 'price': 50.25, 'stock': 50},
        ]
        return mock_response_data

    except requests.exceptions.RequestException as e:
        # This block would catch network errors in a real application
        print(f"An error occurred while fetching data: {e}")
        return None
    except json.JSONDecodeError:
        print("Failed to decode JSON from the response.")
        return None

