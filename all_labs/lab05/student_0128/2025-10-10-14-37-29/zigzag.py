# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag(int_list):
    evil_not_zigzag_perchance = 0
    for i in range(1,len(int_list) - 1):
        if not((int_list[i] > int_list[i + 1] and int_list[i] > int_list[i - 1]) or (int_list[i] < int_list[i + 1] and int_list[i] < int_list[i - 1])):
            evil_not_zigzag_perchance += 1
    return not bool(evil_not_zigzag_perchance)