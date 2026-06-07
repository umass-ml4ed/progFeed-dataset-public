# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(int_list):
    if len(int_list) < 3:
        return True
    counter = 0
    for integer in int_list[1:-1]:
        if (integer < int_list[counter] and integer < int_list[counter + 2]) or (integer > int_list[counter] and integer > int_list[counter + 2]):
            counter += 1
        else:
            return False
    return True