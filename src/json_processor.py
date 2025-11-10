#!/usr/bin/env python3
"""
json_processor.py - Work with JSON data
"""

import json
from datetime import datetime

# Sample data (like API response)
client_data = {
    "client_id": "ACME001",
    "name": "Acme Corporation",
    "projects": [
        {
            "name": "Invoice Automation",
            "status": "active",
            "budget": 15000,
            "hours_saved_weekly": 25
        },
        {
            "name": "Email Classification",
            "status": "completed",
            "budget": 8000,
            "hours_saved_weekly": 15
        }
    ],
    "contact": {
        "name": "John Smith",
        "email": "john@acme.com",
        "phone": "+43 123 456789"
    }
}

def save_json(data, filename):
    """Save data to a JSON file"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to {filename}")

def load_json(filename):
    """Load data from a JSON file"""
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def analyze_client_data(data):
    """Analyze client project data"""
    print("\n" + "=" * 50)
    print(f"CLIENT REPORT: {data['name']}")
    print("=" * 50)

    total_budget = sum(p['budget'] for p in data['projects'])
    total_hours_saved = sum(p['hours_saved_weekly'] for p in data['projects'])
    annual_value = total_hours_saved * 52 * 30  # Assuming €30/hour

    print(f"\nTotal Investment: €{total_budget:,}")
    print(f"Weekly Hours Saved: {total_hours_saved} hours")
    print(f"Annual Value: €{annual_value:,}")
    print(f"ROI: {(annual_value / total_budget * 100):.1f}%")

    print("\nProjects:")
    for project in data['projects']:
        print(f" {project['name']}")
        print(f"  - Status: {project['status']}")
        print(f"  - Budget: €{project['budget']:,}")
        print(f"  - Hours Saved: {project['hours_saved_weekly']} hours/week")

    print(f"\nContact: {data['contact']['name']}")
    print(f" Email: {data['contact']['email']}")
    print("=" * 50)

# Main execution
if __name__ == "__main__":
    # Save sample data to JSON
    save_json(client_data, 'data/client_acme.json')

    # Load data back
    loaded_data = load_json('data/client_acme.json')

    # Analyze loaded data
    analyze_client_data(loaded_data)