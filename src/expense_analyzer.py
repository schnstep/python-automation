#!/usr/bin/env python3
"""
expense_analyzer.py - Analyze expense data
"""

import csv
from collections import defaultdict
def read_expenses_basic(filename):
    """Read CSV file using basic Python (no pandas)"""
    expenses = []

    with open(filename, 'r') as file:
        # Create CSV reader
        reader = csv.DictReader(file)

        # Read each row
        for row in reader:
            # Convert amount to float
            row['Amount'] = float(row['Amount'])
            expenses.append(row)

    return expenses

def analyze_expenses(expenses):
    """Calculate statistics from expenses"""
    # Total spent
    total = sum(expense['Amount'] for expense in expenses)

    # Spending by category
    by_category = defaultdict(float)
    for expense in expenses:
        by_category[expense['Category']] += expense['Amount']

    # Average expense
    average = total / len(expenses) if expenses else 0

    return {
        'total': total,
        'average': average,
        'by_category': dict(by_category),
        'count': len(expenses)
    }

def print_summary(stats):
    """Print formatted expense summary"""
    print("\n" + "=" * 50)
    print("EXPENSE ANALYSIS REPORT")
    print("=" * 50)
    print(f"\nTotal_Expenses: €{stats['total']:.2f}")
    print(f"Number of Transactions: {stats['count']}")
    print(f"Average Transaction: €{stats['average']:.2f}")
    print("\nSpending by Category:")

    for category, amount in sorted(stats['by_category'].items(), key=lambda x: x[1], reverse=True):
        percentage = (amount / stats['total']) * 100
        print(f" {category:15} €{amount:8.2f} ({percentage:5.1f}%)")

    print("=" * 50)

# Main execution
if __name__ == "__main__":
    expenses = read_expenses_basic('data/expenses.csv')
    stats = analyze_expenses(expenses)
    print_summary(stats)