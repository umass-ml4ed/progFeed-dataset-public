# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(numbers):
    if len(numbers) < 3:
        return True
    for i in range(1, len(numbers) - 1):
        if not ((numbers[i] >  numbers[i - 1] and  numbers[i] > numbers[i + 1]) or (numbers[i] < numbers[i -1] and numbers[i] < numbers[i +1])):
            return False
    return True

print(is_zigzag([1, 3, 2, 4, 3])) 
print(is_zigzag([1, 4, 2, 5, 3]))  
print(is_zigzag([1, 2, 3, 4]))   
print(is_zigzag([10]))       
print(is_zigzag([1, 3, 2, 4, 5]))  