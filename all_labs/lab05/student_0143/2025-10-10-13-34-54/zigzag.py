# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(list):

    if len(list) == 1:
        return True

    if list[0] < list[1]:
        was_min = False
        last_num = list[0] + 1

    if list[0] > list[1]:
        was_min = True
        last_num = list[1] - 1

    for element in list:
        if element > last_num and was_min == True:
            was_min = False
            last_num = element
            continue
        if element < last_num and was_min == False:
            was_min = True
            last_num = element
            continue
        else:
            return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))    # True
print(is_zigzag([1, 4, 2, 5, 3]))    # True
print(is_zigzag([1, 2, 3, 4]))       # False
print(is_zigzag([10]))               # True
print(is_zigzag([1, 3, 2, 4, 5]))    # Fals
