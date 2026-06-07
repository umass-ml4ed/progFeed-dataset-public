# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED


def filter_positive(numbers):
    
    positive_numbers = []
    
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
        
    return positive_numbers
    

print(filter_positive([1, -3, 5, 0, -2, 7]))
# [1, 5, 7]

print(filter_positive([-5, -1, -10]))
# []

print(filter_positive([10, 20, -30, 40]))
# [10, 20, 40]
