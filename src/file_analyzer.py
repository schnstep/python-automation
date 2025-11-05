#!/usr/bin/env python3
"""
file_analyzer.py - Analyze files in any directory
"""

import os
import sys
from pathlib import Path
from datetime import datetime

def analyze_directory(directory_path):
    """
    Analyze files in a directory and return statistics
    
    Args:
        directory_path: Path to directory to analyze
        
    Returns:
        Dictionary with file statistics
    """
    path = Path(directory_path)
    
    # Check if directory exists
    if not path.exists():
        print(f"Error: Directory '{directory_path}' not found")
        return None
    
    # Initialize counters
    stats = {
        "total_files": 0,
        "total_size": 0,
        "file_types": {},
        "largest_file": {"name": "", "size": 0},
    }

    # Iterate through files
    for item in path.iterdir():
        # Skip hidden files
        if item.name.startswith('.'):
            continue

        if item.is_file():
            stats["total_files"] += 1

            # Get file size
            size = item.stat().st_size
            stats["total_size"] += size

            # Track file types
            extension = item.suffix.lower() or "no extension"
            stats["file_types"][extension] = stats["file_types"].get(extension, 0) + 1

            # Track largest file
            if size > stats["largest_file"]["size"]:
                stats["largest_file"] = {
                    "name": item.name,
                    "size": size
                }
    
    return stats

def format_bytes(bytes_value):
    """Convert bytes to human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.2f} TB"

def print_report(stats):
    """Print formatted analysis report"""
    if not stats:
        return
    
    print("\n" + "=" * 60)
    print("DIRECTORY ANALYSIS REPORT")
    print("=" * 60)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    print(f"Total Files: {stats['total_files']}")
    print(f"Total Size: {format_bytes(stats['total_size'])}")
    print()

    print("File Types:")
    for ext, count in sorted(stats['file_types'].items(), key=lambda x: x[1], reverse=True):
        print(f" {ext:15} {count:5} files")
    print()

    if stats['largest_file']['size'] > 0:
        print("Largest File:")
        print(f" Name: {stats['largest_file']['name']}")
        print(f" Size: {format_bytes(stats['largest_file']['size'])}")

    print("=" * 60)

def main():
    """Main function with command-line argument handling"""
    # Check if directory argument is provided
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.path.expanduser("~/Downloads")

    print(f"Analyzing directory: {directory}")
    stats = analyze_directory(directory)
    print_report(stats)

if __name__ == "__main__":
    main()