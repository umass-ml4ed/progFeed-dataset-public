# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(strings, n): 
    count = 0
    for string in strings: 
        if len(string) >= n: 
            count += 1
    return count


print(count_strings(['', 'a', 'aa', 'aaa'], 0))