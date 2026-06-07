# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst: list) -> bool:
    if len(lst) <= 2:
        return True
    checklist = []
    i = 0
    for num in lst:
        if i == 0:
            if num < lst[i + 1] or num > lst[i + 1]:
                checklist.append(True)
            else:
                checklist.append(False)
        elif i + 1 == len(lst):
            if num < lst[i - 1] or num > lst[i - 1]:
                checklist.append(True)
            else:
                checklist.append(False)
        else:
            if (num > lst[i - 1] and num > lst[i + 1]) or (num < lst[i - 1] and num < lst[i + 1]):
                checklist.insert(-2, True)
            else:
                checklist.insert(-2, False)
        i += 1
    return False not in checklist

print(is_zigzag([1, 3, 2, 4, 3]))    # True
print(is_zigzag([1, 4, 2, 5, 3]))    # True
print(is_zigzag([1, 2, 3, 4]))       # False
print(is_zigzag([10]))               # True
print(is_zigzag([1, 3, 2, 4, 5]))    # False