# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# zigzag.py
# Author: REDACTED
# Date: [Date]
# Description: Function to check if a list follows a zigzag pattern

def is_zigzag(numbers):
   
    # Lists with fewer than 3 elements are always zigzag
    if len(numbers) < 3:
        return True
    
    # Check each middle element
    for i in range(1, len(numbers) - 1):
        left = numbers[i - 1]
        middle = numbers[i]
        right = numbers[i + 1]
        
        # Check if middle is a peak (greater than both neighbors)
        is_peak = middle > left and middle > right
        
        # Check if middle is a valley (smaller than both neighbors)
        is_valley = middle < left and middle < right
        
        # If middle is neither a peak nor a valley, not zigzag
        if not is_peak and not is_valley:
            return False
    
    return True

