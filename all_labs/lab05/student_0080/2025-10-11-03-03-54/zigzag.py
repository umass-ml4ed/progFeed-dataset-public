# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(numbers):
    
    if len(numbers) < 3:
        return True
    
    for i in range(1, len(numbers) - 1):
        current = numbers[i]
        prev = numbers[i - 1]
        next = numbers[i + 1]
        
        if not ((current > prev and current > next) or 
                (current < prev and current < next)):
            return False
    
    return True

# Test cases
if __name__ == "__main__":
    print(is_zigzag([1, 3, 2, 4, 3]))    # True 
    print(is_zigzag([1, 4, 2, 5, 3]))    # True 
    print(is_zigzag([1, 2, 3, 4]))       # False 
    print(is_zigzag([10]))               # True 
    print(is_zigzag([1, 3, 2, 4, 5]))    # False
    print(is_zigzag([]))                 # True (edge case: empty list)
    print(is_zigzag([1, 2]))             # True (edge case: 2 elements)