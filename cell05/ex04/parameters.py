#!/usr/bin/env python
import sys

def main():
    """Display the number of parameters passed to the script."""
    # Get the number of parameters (excluding the script name)
    num_parameters = len(sys.argv) - 1
    
    # Display the count of parameters
    print(f"Number of parameters: {num_parameters}.")

if __name__ == "__main__":
    main()