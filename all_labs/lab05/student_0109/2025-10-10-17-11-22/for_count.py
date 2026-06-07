#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def count_strings(lst,n):
    count = 0
    for item in lst:
        if len(item) >= n:
            count += 1
    return count

