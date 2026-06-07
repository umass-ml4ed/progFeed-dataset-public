# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# zigzag.py
# Student: [Your Name]
# Date: [Current Date]
# Description: Function to check if a list follows a zigzag pattern

def is_zigzag(numbers):
    # Lists with fewer than 3 elements are always zigzag
    if len(numbers) < 3:
        return True
    
    # Check all middle elements (from index 1 to len(numbers)-2)
    for i in range(1, len(numbers) - 1):
        current = numbers[i]
        left_neighbor = numbers[i - 1]
        right_neighbor = numbers[i + 1]
        
        # Check if current element is either:
        # 1. Greater than both neighbors, OR
        # 2. Smaller than both neighbors
        is_peak = (current > left_neighbor) and (current > right_neighbor)
        is_valley = (current < left_neighbor) and (current < right_neighbor)
        
        # If neither condition is true, it's not zigzag
        if not (is_peak or is_valley):
            return False
    
    # All middle elements satisfy the zigzag condition
    return True
print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False


