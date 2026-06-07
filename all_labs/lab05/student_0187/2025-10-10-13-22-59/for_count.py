# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(words, n):
    total = 0
    for w in words:
        if len(w) >= n:
            total = total + 1
    return total

#print(count_strings(['', 'a', 'aa', 'aaa'], 0))   
#print(count_strings(['', 'a', 'aa', 'aaa'], 2))
#print(count_strings(['', 'a', 'aa', 'aaa'], 4))

