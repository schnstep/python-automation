#!/usr/bin/env python3
"""
error_examples.py - Common errors and how to handle them
"""

# Error 1: FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")

# Error 2: ValueError (wrong data type)
try:
    number = int("not a number")
except ValueError:
    print("Error: Cannot convert to integer!")

# Error 3: ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Error 4: KeyError (missing dictionary key)
data = {"name": "Alice"}
try:
    email = data["email"]
except KeyError:
    print("Error: Key 'email' not found in dictionary!")

# Error 5: IndexError (list index out of range)
items = [1, 2, 3]
try:
    value = items[10]
except IndexError:
    print("Error: List index out of range!")

# Multiple exception types
try:
    filename = "data.txt"
    with open(filename, "r") as file:
        number = int(file.read())
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except ValueError:
    print("Error: The file content is not a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
