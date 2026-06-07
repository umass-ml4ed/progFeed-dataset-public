# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(list_of_strings, n):
    count = 0 
    for str in list_of_strings:
        if len(str) >= n:
            count = count + 1 

    return count 

