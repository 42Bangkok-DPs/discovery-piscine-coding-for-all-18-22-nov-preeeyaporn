#!/usr/bin/env python
import sys

def main():
    """Display the first string parameter or 'none' if no parameters are passed."""
    # Check if there are any parameters
    if len(sys.argv) > 1:
        # Display the first parameter (excluding the script name)
        print(sys.argv[1])
    else:
        # Display "none" if no parameters are passed
        print("none")

if __name__ == "__main__":
    main()