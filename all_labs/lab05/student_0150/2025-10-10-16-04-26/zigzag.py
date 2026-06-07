# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst):
    counter = 0
    for n in lst:
        if counter == 0 or counter == (len(lst)-1):
            counter += 1
        else:
            if n >= lst[counter - 1] and n >= lst[counter + 1]:
                counter += 1
            elif n <= lst[counter - 1] and n <= lst[counter + 1]:
                counter += 1
            else:
                return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False

