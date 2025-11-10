#!/usr/bin/env python3
"""
expense_analyzer_pandas.py - Analyze expense data using pandas
"""
import pandas as pd
from datetime import datetime

def read_expenses_pandas(filename):
    """Read CSV file using pandas"""
    # Read CSV
    df = pd.read_csv(filename)

    # Convert 'Date' to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    return df

def analyze_with_pandas(df):
    """Analyze expenses using pandas"""
    print("\n" + "=" * 50)
    print("EXPENSE ANALYSIS REPORT (PANDAS)")
    print("=" * 50)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Basic statistics
    print(f"Total Expenses: €{df['Amount'].sum():.2f}")
    print(f"Number of Transactions: {len(df)}")
    print(f"Average Transaction: €{df['Amount'].mean():.2f}")
    print(f"Median Transaction: €{df['Amount'].median():.2f}")
    print(f"Largest Expense: €{df['Amount'].max():.2f}")
    print(f"Smallest Expense: €{df['Amount'].min():.2f}")
    print()

    # Spending by category
    category_summary = df.groupby('Category')['Amount'].agg(['sum', 'count', 'mean'])
    category_summary = category_summary.sort_values('sum', ascending=False)

    for category, row in category_summary.iterrows():
        percentage = (row['sum'] / df['Amount'].sum()) * 100
        print(f" {category:15} €{row['sum']:8.2f} ({int(row['count'])} txns, avg: €{row['mean']:.2f}) - {percentage:.1f}%")
    print()

    # Date range
    print(f"Date Range: {df['Date'].min().strftime('%Y-%m-%d')} to {df['Date'].max().strftime('%Y-%m-%d')}")

    # Top 5 expenses
    print("\nTop 5 Expenses:")
    top5 = df.nlargest(5, 'Amount')[['Date', 'Category', 'Description', 'Amount']]
    for idx, row in top5.iterrows():
        print(f" {row['Date'].strftime('%Y-%m-%d')} | {row['Category']:10} | {row['Description']:20} | €{row['Amount']:.2f}")

    print("=" * 50)

def export_summary(df, output_file='data/expense_summary.txt'):
    """Export summary to text file"""
    with open(output_file, 'w') as f:
        f.write("EXPENSE ANALYSIS REPORT (PANDAS)\n")
        f.write("=" * 50 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write(f"Total Expenses: €{df['Amount'].sum():.2f}\n")
        f.write(f"Number of Transactions: {len(df)}\n")
        f.write(f"Average Transaction: €{df['Amount'].mean():.2f}\n")

        f.write("Spending by Category:\n")
        category_summary = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
        for category, amount in category_summary.items():
            f.write(f" {category} €{amount:.2f}\n")
    
    print(f"\nSummary exported to {output_file}")

# Main execution
if __name__ == "__main__":
    df = read_expenses_pandas('data/expenses.csv')
    analyze_with_pandas(df)
    export_summary(df)