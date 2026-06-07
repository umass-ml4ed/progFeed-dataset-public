# Name     : REDACTED_NAME
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(listy, n):
    i = 0
    for stringy in listy:
        if len(stringy) >= n:
            i+=1
        else:
            continue
    return i