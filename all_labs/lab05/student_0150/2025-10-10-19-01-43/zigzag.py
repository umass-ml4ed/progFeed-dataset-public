# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst):
    counter = 0
    for n in lst:
        if counter == 0 or counter == (len(lst)-1):
            counter += 1
        else:
            if n > lst[counter - 1] and n > lst[counter + 1]:
                counter += 1
            elif n < lst[counter - 1] and n < lst[counter + 1]:
                counter += 1
            else:
                return False
    return True

print(is_zigzag([1, 2, 2, 3]))    # False


