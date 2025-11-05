#!/usr/bin/env python3
"""
hello_automation.py - Introduction to Python automation
"""

# Variables
name = "AI Consultant"
hours_saved_per_week = 30
hourly_rate = 30.0
annual_value = hours_saved_per_week * 52 * hourly_rate

# Print output
print("=" * 50)
print(f"Welcome, {name}!")
print(f"Your automation saves: {hours_saved_per_week} hours/week")
print(f"Annual value: €{annual_value:,.2f}")
print("=" * 50)

# Data types
text = "string"
number = 42
decimal = 3.14
is_active = True
nothing = None

# Lists
file_types = ["pdf", "docx", "xlsx"]
print(f"\nSupported file types: {file_types}")

# Dictionaries
client = {
    "name": "Acme Corp",
    "industry": "Manufacturing",
    "employees": 150
}
print(f"\nClient: {client['name']}")
print(f"Industry: {client['industry']}")

# Loops
print("\nProcessing file types:")
for file_type in file_types:
    print(f" - Processing {file_type} files...")

# Conditionals 
budget = 5000
if budget > 10000:
    print("\nLarge project")
elif budget > 5000:
    print("\nMedium project")
else:
    print("\nSmall project")

# Functions
def calculate_roi(hours_saved, hourly_rate):
    """Calculate annual ROI of automation"""
    annual_hours = hours_saved * 52
    annual_value = annual_hours * hourly_rate
    return annual_value

# Call Function
roi = calculate_roi(30, 30)
print(f"\nCalculated ROI: {roi:,.2f}")