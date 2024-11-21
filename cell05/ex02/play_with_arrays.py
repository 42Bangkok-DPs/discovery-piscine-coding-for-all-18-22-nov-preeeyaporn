#!/usr/bin/env python
def play_with_arrays():
    """Create and display original and modified arrays with unique values in the new array."""
    # Define the original array
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    
    # Build a new array by adding 2 to each value of the original array
    new_array = [x + 2 for x in original_array]
    
    # Convert the new array to a set to remove duplicates
    unique_new_array = set(new_array)
    
    # Display both arrays
    print(original_array)
    print(unique_new_array)

if __name__ == "__main__":
    play_with_arrays()