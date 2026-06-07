# Author : REDACTED
# Email : REDACTED
# SPIRE ID : REDACTED

def is_zigzag(numbers):
    if len(numbers) < 3:
        return True

    for i in range(1, len(numbers) - 1):
        prev = numbers[i - 1]
        curr = numbers[i]
        next_ = numbers[i + 1]

        if not ((curr > prev and curr > next_) or (curr < prev and curr < next_)):
            return False  
    return True
