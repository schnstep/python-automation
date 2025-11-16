#!/usr/bin/env python3
"""
api_client.py - Reusable API client class
"""

import requests
import json
from typing import Dict, Optional
import time

class APIClient:
    """Generic API client with error handling and retries"""

    def __init__(self, base_url: str, api_key: Optional[str] = None):
        """
        Initialize API client
        
        Args:
            base_url: Base URL for API (e.g., 'https://api.example.com')
            api_key: Optional API key for authentication
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()

        # Set default headers
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'Python-APIClient/1.0'
        })

        # Add API key to headers if provided
        if self.api_key:
            self.session.headers['Authorization'] = f'Bearer {api_key}'

    def get(self, endpoint: str, params: Optional[Dict] = None, retries: int = 3):
        """
        Make GET request
        
        Args:
            endpoint: API endpoint (e.g., '/users/123')
            params: Query parameters
            retries: Number of retry attempts
        """
        url = f"{self.base_url}{endpoint}"

        for attempt in range(retries):
            try:
                response = self.session.get(url, params=params, timeout=10)
                response.raise_for_status()  # Raise error for bad responses
                return response.json()
            
            except requests.exceptions.Timeout:
                if attempt < retries - 1:
                    wait_time = 2 ** attempt # Exponential backoff
                    print(f"⏳ Timeout, retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    print("❌ Error: Request timed out after retries")
                    return None
            
            except requests.exceptions.HTTPError as e:
                print(f"❌ HTTP Error: {e}")
                return None
            
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                return None
            
    def post(self, endpoint: str, data: Dict, retries: int = 3):
        """Make POST request"""
        url = f"{self.base_url}{endpoint}"

        for attempt in range(retries):
            try:
                response = self.session.post(url, json=data, timeout=10)
                response.raise_for_status()
                return response.json()
            
            except Exception as e:
                if attempt < retries - 1:
                    wait_time = 2 ** attempt
                    print(f"⏳ Error occurred, retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    print(f"❌ Unexpected error: {e}")
                    return None

# Example usage with public API
if __name__ == "__main__":
    # JSONPlaceholder - free fake API for testing
    client = APIClient("https://jsonplaceholder.typicode.com")

    # GET request example
    print("Fetching user data...")
    user = client.get("/users/1")
    if user:
        print(f"User: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Company: {user['company']['name']}")

    # GET with parameters example
    print("\nFetching posts...")
    posts = client.get("/posts", params={"userId": 1})
    if posts:
        print(f"Found {len(posts)} posts")
        print(f"First post: {posts[0]['title']}")

    # POST request example
    print("\nCreating a new post...")
    new_post = {
        "title": "Automation with Python",
        "body": "Learning API integration",
        "userId": 1
    }
    result = client.post("/posts", new_post)
    if result:
        print(f"Created post ID: {result['id']}")