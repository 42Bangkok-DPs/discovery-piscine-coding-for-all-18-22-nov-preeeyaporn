#!/usr/bin/env python
def play_with_arrays():
    """Create and display original and modified arrays with filtered and unique values."""
    # Define the original array
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    
    # Filter values greater than 5 and add 2 to each of them
    new_array = [x + 2 for x in original_array if x > 5]
    
    # Convert the new array to a set to remove duplicates
    unique_new_array = set(new_array)
    
    # Display both arrays
    print(original_array)        # Original array
    print(unique_new_array)      # New array as a set (duplicates removed)

if __name__ == "__main__":
    play_with_arrays()