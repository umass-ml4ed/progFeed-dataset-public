# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(int_list):
    if len(int_list) < 3:
        return True
    for i in range(1, len(int_list) - 1):
        if not ((int_list[i] > int_list[i - 1] and int_list[i] > int_list[i + 1]) or (int_list[i] < int_list[i - 1] and int_list[i] < int_list[i + 1])):
            return False
    return True
