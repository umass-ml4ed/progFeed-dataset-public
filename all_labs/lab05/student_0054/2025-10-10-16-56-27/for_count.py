# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

"""Your first exercise is to write a
function called count_strings which takes a 
list of strings and an integer n, and returns how
many strings in the list contain at least n characters."""

def count_strings(string_, n):
    count = 0
    for s in string_:
        if len(s) >= n:
            count += 1
    return count