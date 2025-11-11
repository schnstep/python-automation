#!/usr/bin/env python3
"""
expense_analyzer_robust.py - Expense analyzer with error handling
"""

import pandas as pd
import sys
from pathlib import Path

def validate_file(filename):
    """
    Validate file exists and is readable
    
    Returns:
        Path object if valid, None otherwise
    """
    filepath = Path(filename)
    
    if not filepath.exists():
        print(f"❌ Error: File '{filename}' not found")
        return None
    
    if not filepath.is_file():
        print(f"❌ Error: '{filename}' is not a file")
        return None
    
    if filepath.stat().st_size == 0:
        print(f"❌ Error: File '{filename}' is empty")
        return None
    
    return filepath

def read_expenses_safe(filename):
    """
    Safely read expense CSV with error handling
    
    Returns:
        DataFrame if successful, None otherwise
    """
    # Validate file first
    filepath = validate_file(filename)
    if filepath is None:
        return None
    
    try:
        # Attempt to read CSV
        df = pd.read_csv(filepath)
        
        # Validate required columns exist
        required_columns = ['Date', 'Category', 'Description', 'Amount']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            print(f"❌ Error: Missing required columns: {', '.join(missing_columns)}")
            print(f"   Found columns: {', '.join(df.columns)}")
            return None
        
        # Convert Amount to numeric, handle errors
        df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
        
        # Check for invalid amounts
        invalid_rows = df[df['Amount'].isna()]
        if len(invalid_rows) > 0:
            print(f"⚠️  Warning: Found {len(invalid_rows)} rows with invalid amounts")
            print("   These rows will be excluded from analysis")
            df = df.dropna(subset=['Amount'])
        
        # Convert dates
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        
        # Check for invalid dates
        invalid_dates = df[df['Date'].isna()]
        if len(invalid_dates) > 0:
            print(f"⚠️  Warning: Found {len(invalid_dates)} rows with invalid dates")
            df = df.dropna(subset=['Date'])
        
        if len(df) == 0:
            print("❌ Error: No valid data rows after validation")
            return None
        
        print(f"✅ Successfully loaded {len(df)} valid expense records")
        return df
        
    except pd.errors.EmptyDataError:
        print("❌ Error: CSV file is empty")
        return None
        
    except pd.errors.ParserError as e:
        print(f"❌ Error: Failed to parse CSV file")
        print(f"   Details: {e}")
        return None
        
    except Exception as e:
        print(f"❌ Unexpected error reading file: {e}")
        return None

def analyze_expenses(df):
    """Analyze expenses with error handling"""
    if df is None or len(df) == 0:
        print("❌ Error: No data to analyze")
        return None
    
    try:
        stats = {
            'total': df['Amount'].sum(),
            'count': len(df),
            'average': df['Amount'].mean(),
            'by_category': df.groupby('Category')['Amount'].sum().to_dict()
        }
        return stats
        
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        return None

def print_report(stats):
    """Print expense report"""
    if stats is None:
        return
    
    print("\n" + "=" * 50)
    print("EXPENSE ANALYSIS REPORT")
    print("=" * 50)
    print(f"\nTotal Expenses: €{stats['total']:.2f}")
    print(f"Number of Transactions: {stats['count']}")
    print(f"Average Transaction: €{stats['average']:.2f}")
    
    print("\nSpending by Category:")
    for category, amount in sorted(stats['by_category'].items(), key=lambda x: x[1], reverse=True):
        percentage = (amount / stats['total']) * 100
        print(f"  {category:15} €{amount:8.2f} ({percentage:5.1f}%)")
    
    print("=" * 50)

def main():
    """Main function with command-line argument handling"""
    # Get filename from command line or use default
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'data/expenses.csv'
    
    print(f"Analyzing expenses from: {filename}")
    
    # Process with error handling
    df = read_expenses_safe(filename)
    
    if df is not None:
        stats = analyze_expenses(df)
        print_report(stats)
        return 0  # Success
    else:
        print("\n❌ Analysis failed")
        return 1  # Error

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)