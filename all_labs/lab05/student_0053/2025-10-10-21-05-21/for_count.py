# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def count_strings(l: list, n: int) -> int:
    '''This function will return how many strings in the list that have at
    least n characters, and input n should be a natural number.'''
    
    count = 0
    for str in l:
        if len(str) >= n:
            count += 1
    return count
