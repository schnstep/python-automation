#!/usr/bin/env python3
"""
custom_exceptions.py - Create custom exception types
"""

# Custom exception classes
class DataValidationError(Exception):
    """Raised when data fails validation"""
    pass

class InsufficientDataError(Exception):
    """Raised when not enough data for analysis"""
    pass

class ConfigurationError(Exception):
    """Raised when configuration is invalid"""
    pass

def process_expense_data(data):
    """Process expense data with custom exceptions"""
    
    # Check if we have data
    if not data or len(data) == 0:
        raise InsufficientDataError("No expense records provided")
    
    # Check for required fields
    required_fields = ['date', 'amount', 'category']
    for record in data:
        missing_fields = [f for f in required_fields if f not in record]
        if missing_fields:
            raise DataValidationError(
                f"Record missing required fields: {', '.join(missing_fields)}"
            )
    
    # Check amounts are positive
    for record in data:
        if record['amount'] <= 0:
            raise DataValidationError(
                f"Invalid amount: {record['amount']} (must be positive)"
            )
    
    return True

# Test custom exceptions
if __name__ == "__main__":
    # Valid data
    try:
        valid_data = [
            {'date': '2025-10-01', 'amount': 100, 'category': 'Food'}
        ]
        process_expense_data(valid_data)
        print("✅ Valid data processed successfully")
    except (DataValidationError, InsufficientDataError) as e:
        print(f"❌ Validation failed: {e}")
    
    # Empty data
    try:
        process_expense_data([])
    except InsufficientDataError as e:
        print(f"❌ Expected error: {e}")
    
    # Missing field
    try:
        invalid_data = [
            {'date': '2025-10-01', 'amount': 100}  # Missing category
        ]
        process_expense_data(invalid_data)
    except DataValidationError as e:
        print(f"❌ Expected error: {e}")
    
    # Invalid amount
    try:
        invalid_data = [
            {'date': '2025-10-01', 'amount': -50, 'category': 'Food'}
        ]
        process_expense_data(invalid_data)
    except DataValidationError as e:
        print(f"❌ Expected error: {e}")