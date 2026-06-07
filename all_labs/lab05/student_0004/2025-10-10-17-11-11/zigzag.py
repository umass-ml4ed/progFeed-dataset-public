def is_zigzag(numbers):
    
    if len(numbers) < 3:
        return True

    for i in range(1, len(numbers) - 1):
        left = numbers[i - 1]
        mid = numbers[i]
        right = numbers[i + 1]

        if not ((mid > left and mid > right) or (mid < left and mid < right)):
            return False

    return True


print(is_zigzag([1, 3, 2, 4, 3]))  # True
print(is_zigzag([1, 4, 2, 5, 3]))  # True
print(is_zigzag([1, 2, 3, 4]))     # False
print(is_zigzag([10]))             # True
print(is_zigzag([1, 3, 2, 4, 5]))  # False
