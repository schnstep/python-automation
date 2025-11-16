#!/usr/bin/env python3
"""
secure_api_usage.py - Using environment variables for secrets
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access API keys securely
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

if not WEATHER_API_KEY:
    print("⚠️  Warning: WEATHER_API_KEY not set in .env file")
    WEATHER_API_KEY = "demo_key"  # Use demo key

print("Environment variables loaded:")
print(f" Weather API Key: {'*' * 8}{WEATHER_API_KEY[-4:] if WEATHER_API_KEY else 'Not Set'}")
print(f" GitHub Token: {'Set' if GITHUB_TOKEN else 'Not Set'}")

# Use in API calls

def make_secure_api_call():
    """Example of secure API usage"""
    import requests

    headers = {
        'Authorization': f'Bearer {WEATHER_API_KEY}',
        'Content-Type': 'application/json'
    }
    # API call here...
    print("✅ API call made securely with environment variable")

if __name__ == "__main__":
    make_secure_api_call()