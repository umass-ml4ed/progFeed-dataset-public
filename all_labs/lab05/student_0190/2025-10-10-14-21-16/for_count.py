# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lst, num):
    count = 0
    for string in lst:
        if len(string) >= num:
            count += 1
    return count

print(count_strings(['', 'a', 'aa', 'aaa'], 4))
