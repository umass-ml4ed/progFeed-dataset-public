# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def is_zigzag(numbers):
    # Lists with fewer than 3 elements are automatically zigzag
    if len(numbers) < 3:
        return True

    # Loop through all middle elements (1 to len(numbers) - 2)
    for i in range(1, len(numbers) - 1):
        # Check if current element is either a "peak" or a "valley"
        if not ((numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]) or
                (numbers[i] < numbers[i - 1] and numbers[i] < numbers[i + 1])):
            return False  # breaks zigzag pattern
    return True

print(is_zigzag([1, 3, 2, 4, 3]))  # True
print(is_zigzag([1, 4, 2, 5, 3]))  # True
print(is_zigzag([1, 2, 3, 4]))     # False
print(is_zigzag([10]))             # True
print(is_zigzag([1, 3, 2, 4, 5]))  # False
