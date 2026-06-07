# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(lst_of_strings, integer):
    good_strings = 0
    for string in lst_of_strings:
        if len(string) >= integer:
            good_strings += 1
    return good_strings