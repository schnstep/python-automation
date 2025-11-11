#!/usr/bin/env python3
"""
complete_error_handling.py - Complete error handling pattern
"""

def process_file(filename):
    """Process a file with complete error handling
    
    try: Code that might raise an exception
    except: Handle specific exceptions
    else: Code to run if no exceptions occur
    finally: Code that always runs (cleanup code)
    """
    print(f"\nProcessing: {filename}")
    
    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()
            lines = len(content.split('\n'))
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    
    except PermissionError:
        print(f"Error: No permission to read '{filename}'.")
        return None
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
    else:
        # Only runs if no exception occurred
        print(f"Successfully read {lines} lines.")
        return content
    
    finally:
        # Always runs (even if exception or return)
        print(f"Finished processing attempt for: {filename}")

# Test with various files
if __name__ == "__main__":
    # File that exists
    result1 = process_file('data/expenses.csv')
    # File that does not exist
    result2 = process_file('data/missing_file.txt')
    # Current script (should work)
    resutlt3 = process_file(__file__)
