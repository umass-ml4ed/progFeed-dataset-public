# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(numbers):
    if len(numbers) < 3:
        return True
    
    for i in range (1, len(numbers) - 1 ):
        prev_num = numbers[i - 1]
        current_num = numbers[i]
        next_num = numbers[i + 1]
    
    if not ((current_num > prev_num and current_num > next_num) or (current_num < prev_num and current_num < next_num)):
        return False

    return True

print(is_zigzag([1, 3, 2, 4, 3]))  
print(is_zigzag([1, 4, 2, 5, 3]))  
print(is_zigzag([1, 2, 3, 4]))     
print(is_zigzag([10]))             
print(is_zigzag([1, 3, 2, 4, 5]))  