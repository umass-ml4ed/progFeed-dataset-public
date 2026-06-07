# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def is_zigzag(numbers):
    if len(numbers) < 3:
        return True
    for i in range(1, len(numbers) - 1):
        if not ((numbers [i] > numbers [i - 1] and numbers[i] > numbers[i + 1]) or 
                (numbers [i] < numbers[i - 1] and numbers[i] < numbers[i + 1])):
            return False
    return True
    

