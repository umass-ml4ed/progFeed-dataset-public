# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lst, n):
    for string in lst:
        if len(string) > n:
            n += 1
    return n

print(count_strings(['hi', 'hello', 'hey', 'greetings'], 3))

