# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag(l_of_n):
    if len(l_of_n):
        return True
    for i in range(1, len(l_of_n) -1):
        below = l_of_n[i - 1]
        medium = l_of_n[i]
        above = l_of_n[i + 1]
        if not ((medium > below and medium > above) or (medium < below and medium < above)):
            return False
    return True
        