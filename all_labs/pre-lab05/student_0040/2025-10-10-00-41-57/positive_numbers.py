# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
import math

def filter_positive(numbers):
    positive_numbers = []
    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
    return positive_numbers