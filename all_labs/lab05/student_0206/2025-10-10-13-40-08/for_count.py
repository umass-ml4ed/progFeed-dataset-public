# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(l: list, i: int):
    hive = 0
    for char in l:
        if len(char) >= i:
            hive += 1
    return hive
print(count_strings(['', 'a', 'aa', 'aaa'], 0))