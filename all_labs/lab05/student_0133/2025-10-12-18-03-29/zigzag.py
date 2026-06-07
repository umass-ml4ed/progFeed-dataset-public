# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag(numbers):
    if len(numbers) < 3:
        return True
    
    for i in range(1, len(numbers) - 1):
        prev = numbers[i-1]
        curr = numbers[i]
        next_ = numbers[i+1]

        if not ((curr > prev and curr > next_) or (curr < prev and curr < next_)):
            return False
        
    return True    
    
    

print(is_zigzag([1, 3, 2, 4, 3]))
print(is_zigzag([1, 4, 2, 5, 3]))
print(is_zigzag([1, 2, 3, 4]))
