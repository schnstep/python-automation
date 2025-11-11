#!/usr/bin/env python3
"""
expense_analyzer_with_logging.py - Add logging for debugging
"""

import pandas as pd
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("expense_analyzer.log"),
        logging.StreamHandler() # Also print to console
    ]
)

logger = logging.getLogger(__name__)

def read_expenses(filename):
    """Read expenses with logging"""
    logger.info(f"Starting to read file: {filename}")
    
    try:
        df = pd.read_csv(filename)
        logger.info(f"Successfully read {len(df)} rows from {filename}")
        
        # Log data quality issues
        null_counts = df.isnull().sum()
        if null_counts.any():
            logger.warning(f"Found null values: {null_counts[null_counts > 0].to_dict()}")
        
        return df
        
    except FileNotFoundError:
        logger.error(f"File not found: {filename}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error reading {filename}: {e}")
        raise

def analyze_expenses(df):
    """Analyze with logging"""
    logger.info("Starting expense analysis")
    
    total = df['Amount'].sum()
    count = len(df)
    
    logger.info(f"Total expenses: €{total:.2f}")
    logger.info(f"Transaction count: {count}")
    
    # Log by category
    by_category = df.groupby('Category')['Amount'].sum()
    for category, amount in by_category.items():
        logger.info(f"Category {category}: €{amount:.2f}")
    
    logger.info("Analysis complete")
    
    return {
        'total': total,
        'count': count,
        'by_category': by_category.to_dict()
    }

if __name__ == "__main__":
    logger.info("=" * 60)
    logger.info("Starting expense analyzer")
    logger.info("=" * 60)
    
    try:
        df = read_expenses('data/expenses.csv')
        stats = analyze_expenses(df)
        logger.info("Program completed successfully")
    except Exception as e:
        logger.error(f"Program failed: {e}")
        raise