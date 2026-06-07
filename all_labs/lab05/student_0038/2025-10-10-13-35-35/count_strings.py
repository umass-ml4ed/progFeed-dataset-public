# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(string: str, n: int):
    count = 0
    for i in string: 
        if len(i) >= n: 
            count += 1
    return count
