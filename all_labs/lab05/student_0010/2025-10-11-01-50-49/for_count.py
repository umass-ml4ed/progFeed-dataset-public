# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(list, n):
        count = 0
        ind = 0
        for string in list:
                if len(list[ind]) >= n:
                        count += 1
                ind += 1
        return count
                        



