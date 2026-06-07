# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


#Implement filter_positive

def filter_positive(numbers: list[int]) -> list[int]:
    positive_nums =[]
    for num in numbers:
        if num > 0:
            positive_nums.append(num)
    return positive_nums

print(filter_positive([1, -3, 5, 0, -2, 7]))    # [1, 5, 7]
print(filter_positive([-5, -1, -10]))           # []
print(filter_positive([10, 20, -30, 40]))       # [10, 20, 40]
