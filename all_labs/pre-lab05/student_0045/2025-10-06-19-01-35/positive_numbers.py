# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def filter_positive(numbers):
    positive_numbers = []
    for number in numbers:
        if number>0:
            positive_numbers.append(number)
    return positive_numbers

print(filter_positive([1, -3, 5, 0, -2, 7]))
# [1, 5, 7]

print(filter_positive([-5, -1, -10]))
# []

print(filter_positive([10, 20, -30, 40]))
# [10, 20, 40]
