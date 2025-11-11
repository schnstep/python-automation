#!/usr/bin/env python3
"""
context_managers.py - Safe resource handling
"""

from pathlib import Path
import time

# Traditional approach (risky - file might not close)
def write_file_unsafe(filename, content):
    """Unsafe: file might not close if error occurs"""
    f = open(filename, 'w')
    f.write(content)
    # If error happens here, file never closes!
    f.close()

# Safe approach using context manager
def write_file_safe(filename, content):
    """Safe: file always closes using 'with' context manager"""
    with open(filename, 'w') as f:
        f.write(content)
        # File automatically closed when block ends
        # Even if exeption occurs

# Custom context manager
class Timer:
    """Context manager to time code execution"""
    
    def __enter__(self):
        """Called when entering 'with' block"""
        self.start = time.time()
        print("⏱️  Timer started")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block"""
        self.end = time.time()
        self.duration = self.end - self.start
        print(f"⏱️  Timer stopped: {self.duration:.4f} seconds")
        return False  # Don't suppress exceptions

# Use timer context manager
if __name__ == "__main__":
    # Time a code block
    with Timer():
        # Simulate some work
        total = sum(range(1000000))
        print(f"Calculated sum: {total}")
    
    # Timer automatically prints duration when 'with' block ends
    
    # Multiple context managers
    with Timer(), \
         open('data/test_output.txt', 'w') as f:
        f.write("Testing context managers\n")
        time.sleep(0.5)  # Simulate work
    
    print("\n✅ All resources cleaned up properly")